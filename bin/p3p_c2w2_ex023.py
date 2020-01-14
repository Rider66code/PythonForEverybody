#Create a dictionary called d that keeps track of all the characters in the string placement and notes how many times each character was seen. Then, find the key with the lowest value in this dictionary and assign that key to min_value.
placement = "Beaches are cool places to visit in spring however the Mackinaw Bridge is near. Most people visit Mackinaw later since the island is a cool place to explore."
min_value=''
d={}
for char in placement:
    if char not in d:
        # we have not seen this character before, so initialize a counter for it
        d[char] = 0
    #whether we've seen it before or not, increment its counter
    d[char] = d[char] + 1

ks=d.keys()
min_value=ks[0]
for k in ks:
    if d[k]<d[min_value]:
        min_value=k
print(min_value)
