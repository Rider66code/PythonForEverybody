import json
print(type(res))
print(res.keys())
res2 = res['statuses']
print("----Level 2: a list of tweets-----")
print(type(res2)) # it's a list!
print(len(res2))  # looks like one item representing each of the three tweets
for res3 in res2[:1]:
   print("----Level 3: a tweet----")
   print(json.dumps(res3, indent=2)[:30])
   print(type(res3)) # it's a dictionary
   print(res3.keys())
