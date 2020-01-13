#!/usr/bin/env python3

import json
import subprocess

file = 'parsed_alerts.json'

mx_quote_host=input('Please enter multiplexor quote host (default is tosrs1app1):')
if len(mx_quote_host)<1:
    mx_quote_host='tosrs1app1'
mx_quote_port=input('Please enter multiplexor quote port (default is 7015):')
if len(mx_quote_port)<1:
    mx_quote_port='7015'

connstring=mx_quote_host+':'+mx_quote_port
print('Following multiplexor connection will be used for posting prices:',connstring)

try:
    with open(file) as f:
        alerts = json.load(f)
except:
    print('parsed_alerts.json file not found, exiting.')
    quit()

# we want to post a bare minimum of trades
# Idea: get max price for each symbol and then post
prices = {}
for alert in alerts:
    try:
        prices[alert['symbol']]
    except KeyError:
        prices[alert['symbol']] = 0
    # finding bigger price
    if float(alert['price']) > float(prices[alert['symbol']]):
        prices[alert['symbol']] = float(alert['price'])

print(prices)
#print(alerts)

# qd record example:
# Trade .IBM160219P125 \0 N/A 11000 0 0 N/A N/A
records = []

for s, p in prices.items():
    record = r"Trade {s} \0 N/A {p} 0 0 N/A N/A".format(
        s=s, p=p
    )
    records.append(record)
# for alert in alerts:
#     record = r"Trade {s} \0 N/A {p} 0 0 N/A N/A".format(
#         s=alert['symbol'], p=alert['price']
#     )
#     records.append(record)

command = '\n'.join(records) + '\n'

con = subprocess.Popen(['qds', 'post', str(connstring)], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = con.communicate(bytes(command, 'utf-8'))
out = out.decode().split('\n')
for l in out:
    print(l)
print(err)
