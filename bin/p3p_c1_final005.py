inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
for stockstr in inventory:
    stocklist=stockstr.split(',')
    print('The store has {} {}, each for {} USD.'.format(stocklist[1].strip(),stocklist[0].strip(),stocklist[2].strip()))
