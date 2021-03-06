#!/usr/bin/env python3

import cx_Oracle
import datetime
import argparse
import subprocess
import random
import json

"""
Take a list of available symbols on platform and produce shorter list.
Uses parameters which control symbol's applicability.
Take generated list, create many lines and pass it to console.
Get and parse console output.
"""

#Some Comment

# Requires cx_Oracle, which
# Requires Oracle Client Library - https://oracle.github.io/odpi/doc/installation.html - DS


# 0.1 - Initial Release
# 0.2 - Configuration file added for setting desired parameters
#       Some exception handlers added

__author__ = 'Ilya R. Dementyev, Dmitrii A. Samodurov'
__version__ = '0.2'
__date__ = '2019-01-13'

def rows_to_dict_list(cursor):
    columns = [i[0] for i in cursor.description]
    return [dict(zip(columns, row)) for row in cursor]

def get_symbols(limit=10, days=30):
    global connstring
    """
    :param limit: number of symbols to return
    :param days: number of days to look back for
    :return: list of arrays like {'CNT_ORDERS': 2166, 'SYMBOL': 'IBM', 'INSTRUMENT_ID': '12'}
    """

    sql = """select *
    from (select i.symbol symbol, count(o.order_id) cnt_orders, i.instrument_id instrument_id
        from orders      o,
             order_legs  ol,
             instruments i
        where o.order_id = ol.order_id
            and i.instrument_id = ol.instrument_id
                -- for last {days} calendar days
            and o.order_time >= trunc(sysdate) - {days}
            and (o.close_time > trunc(sysdate) - {days} or o.close_time is null)
                -- exclude FOREX symbols
            and i.type not in ('R', 'H')
        group by i.symbol, i.instrument_id
        order by count(o.order_id) desc)
    where rownum <= {limit}""".format(limit=limit, days=days)
    try:
        con = cx_Oracle.connect(str(connstring))
    except:
        print('Cannot connect to the database, exiting.')
        quit()
    cur = con.cursor()
    cur.execute(sql)
    data = rows_to_dict_list(cur)
    return data

def parse_response(resp):
    # return array for each response
    trash, data = resp.split('{', maxsplit=1)
    data = data.rstrip('}')
    fields = data.split(', ')
    fields_arr = {}
    for f in fields:
        k, v = f.split('=', maxsplit=1)
        fields_arr[k] = v.replace("'", '').replace('"', '')
    #print(fields_arr)
    return {'alert_id': fields_arr['alert_id'],
            'symbol': fields_arr['symbol'],
            'price': fields_arr['price']}

p = argparse.ArgumentParser(
    description="TBF",
    epilog="v{} ({}) by {}".format(__version__, __date__, __author__),
    formatter_class=argparse.RawDescriptionHelpFormatter
)
p.add_argument('-n', '--number', required=True, type=int,
               help="Number of symbols to return")
p.add_argument('-f', '--frequency', required=True, type=int,
               help="Frequency cut-off number (symbol should be traded more "
                    "than this number of times)")
p.add_argument('-d', '--days', type=int, default=100,
               help="Number of days back to use for selection")
p.add_argument('-a', '--alerts', required=True, type=int,
               help="Number of alerts to create")
p.add_argument('-p', '--price', nargs=2, default=[1000, 10000],
               help="2 prices: min & max, separated by space")
args = p.parse_args()

config_file = 'alerter_config.json'
try:
    with open(config_file) as f:
        config = json.load(f)
except:
    print('alerter_config.json file not found, exiting.')
    quit()
print('Configuration file found:',config_file)

db_user=config["db_user"]
db_pass=config["db_pass"]
db_host=config["db_host"]
db_service=config["db_service"]
#login_mask='"'+config["login_mask"]+'"'
login_mask=config["login_mask"]
print('Following user mask will be used for id list generation:',login_mask)
connstring=db_user+'/'+db_pass+'@'+db_host+'/'+db_service
print('Following database connection will be used:',connstring)

cut_off = args.frequency  # M
number = args.number  # N
alert_number = args.alerts  # alerts number
price_range = args.price  # price list
sql = """select * from users where login_name like '{mask}'""".format(
    mask=login_mask)
#symbols_file = 'working_symbols.json'
out_file = 'parsed_alerts.json'

# currently limit is set to 2*N. Incremental logic should be present instead
data = get_symbols(limit=number*2, days=args.days)

symbols = []
n = 0

for pair in data:
    if pair['CNT_ORDERS'] >= cut_off:
        if n < number:
            #print("{}: {}".format(n, pair))
            symbols.append(pair)
        else:
            break
        n += 1
try:
    con = cx_Oracle.connect(str(connstring))
except:
    print('Cannot connect to the database, exiting.')
    quit()
cur = con.cursor()
cur.execute(sql)
users = rows_to_dict_list(cur)

ids = []
time_now = datetime.datetime.now().strftime("%s000")

for i in users:
    print("{u}:{id}".format(u=i['LOGIN_NAME'], id=i['USER_ID']))
    ids.append({'USER_ID': i['USER_ID'], 'LOGIN_NAME': i['LOGIN_NAME']})

commands = []
console = subprocess.Popen('run-console', shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

for n, i in enumerate(range(alert_number)):

    r_user = ids[random.randint(0, len(ids)-1)]
    r_symbol = symbols[random.randint(0, len(symbols)-1)]
    r_price = random.randint(int(price_range[0]), int(price_range[1]))
    spd = 'STOCK'
    if r_symbol['SYMBOL'].startswith('.'):
        spd = 'SINGLE'
    if r_symbol['SYMBOL'].startswith('/'):
        spd = 'FUTURE'
    print("{n:03n}:{t}: User {u}({uid}) is issuing an alert @ symbol={s}({sid}), price={p}, spd={spd}".format(
        n=n, t=time_now, u=r_user['LOGIN_NAME'], uid=r_user['USER_ID'], s=r_symbol['SYMBOL'], sid=r_symbol['INSTRUMENT_ID'], p=r_price,
        spd=spd
    ))
#    commands.append("create-alert t={t} u={u} o=2 f=LAST p={p} spd={spd} smb={s} {{ i={i_id} q=1 }}".format(
    commands.append("create-alert t={t} u={u} o=2 f=LAST p={p} spd={spd} {{ i={i_id} q=1 }}".format(
        t=time_now, u=r_user['USER_ID'], p=r_price, spd=spd, s=r_symbol['SYMBOL'], i_id=r_symbol['INSTRUMENT_ID']
    ))

command = "\n".join(commands)+"\n"
out, err = console.communicate(bytes(command, 'UTF-8'))
out = out.decode().split('\n')

creates = []
responses = []
parsed = []
for line in out:
    if line.startswith('>create-alert'):
        creates.append(line)
    elif line.startswith('This alert was created'):
        responses.append(line)

for r in responses:
    f = parse_response(r)
    parsed.append({'alert_id': f['alert_id'],
                   'symbol': f['symbol'],
                   'price': f['price']})

with open(out_file, 'w') as of:
    print(json.dumps(parsed, sort_keys=True, indent=4), file=of)
