#Below, we have provided the dictionary groceries, whose keys are grocery items, and values are the number of each item that you need to buy at the store. Sort the dictionary’s keys into alphabetical order, and save them as a list called grocery_keys_sorted.
groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
d = {}
for x in groceries:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1
grocery_keys_sorted = sorted(d.keys())
for k in grocery_keys_sorted:
    print("{} appears {} times".format(k, d[k]))
