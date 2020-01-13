#!/usr/bin/env python3

import json
import subprocess

config_file = 'alerter_config.json'
file = 'parsed_alerts.json'

try:
    with open(config_file) as f:
        config = json.load(f)
except:
    print('alerter_config.json file not found, exiting.')
    quit()
print('Configuration file found:',config_file)

try:
    with open(file) as f:
        alerts = json.load(f)
except:
    print('parsed_alerts.json file not found, exiting.')
    quit()
print('Parsed alerts file found:',file)

mx_quote_host=config["mx_quote_host"]
mx_quote_port=config["mx_quote_port"]

connstring=mx_quote_host+':'+mx_quote_port
print('Following multiplexor connection will be used for posting prices:',connstring)

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
