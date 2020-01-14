#Find the least frequent letter. Create the dictionary characters that shows each character from string sally and its frequency. Then, find the least frequent letter in the string and assign the letter to the variable worst_char.
sally = "sally sells sea shells by the sea shore and by the road"
worst_char=''
characters={}
for char in sally:
    if char not in characters:
        # we have not seen this character before, so initialize a counter for it
        characters[char] = 0
    #whether we've seen it before or not, increment its counter
    characters[char] += 1

ks=characters.keys()
worst_char=ks[0]
for k in ks:
    if characters[k]<characters[worst_char]:
        worst_char=k
print(worst_char)
