#Provided is a string saved to the variable name s1. Create a dictionary named counts that contains each letter in s1 and the number of times it occurs.
s1 = "hello"
counts={}
for char in s1:
    if char not in counts:
        # we have not seen this character before, so initialize a counter for it
        counts[char] = 0
    #whether we've seen it before or not, increment its counter
    counts[char] += 1
print(counts)
