#5. Create a dictionary called lett_d that keeps track of all of the characters in the string product and notes how many times each character was seen. Then, find the key with the highest value in this dictionary and assign that key to max_value.
product = "iphone and android phones"
lett_d={}
for char in product:
    if char not in lett_d:
        lett_d[char]=0
    lett_d[char]+=1
    temp_value=lett_d[char]
for char in lett_d:
    if temp_value<lett_d[char]:
        temp_value=lett_d[char]
        max_value=char
print(max_value)
