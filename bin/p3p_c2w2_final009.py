#Create a dictionary called low_d that keeps track of all the characters in the string p and notes how many times each character was seen. Make sure that there are no repeats of characters as keys, such that “T” and “t” are both seen as a “t” for example.
p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
low_d={}
for char in p.lower():
    if char not in low_d:
        # we have not seen this character before, so initialize a counter for it
        low_d[char] = 0
    #whether we've seen it before or not, increment its counter
    low_d[char] += 1
print(low_d)
