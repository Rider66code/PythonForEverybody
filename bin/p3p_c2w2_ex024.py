#Create a dictionary called lett_d that keeps track of all of the characters in the string product and notes how many times each character was seen. Then, find the key with the highest value in this dictionary and assign that key to max_value.
product = "iphone and android phones"
max_value=''
lett_d={}
for char in product:
    if char not in lett_d:
        # we have not seen this character before, so initialize a counter for it
        lett_d[char] = 0
    #whether we've seen it before or not, increment its counter
    lett_d[char] = lett_d[char] + 1
ks=lett_d.keys()
max_value=ks[0]
for k in ks:
    if lett_d[k]>lett_d[max_value]:
        max_value=k
print(max_value)
