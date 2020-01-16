#2. Sort the following dictionary based on the keys so that they are sorted a to z. Assign the resulting value to the variable sorted_keys.
dictionary = {"Flowers": 10, 'Trees': 20, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 14}
d = {}
for x in dictionary:
    if x in d:
        d[x] = d[x] + 1
    else:
        d[x] = 1
sorted_keys = sorted(d.keys())
for k in sorted_keys:
    print("{} appears {} times".format(k, d[k]))
