#Create the dictionary characters that shows each character from the string sally and its frequency. Then, find the most frequent letter based on the dictionary. Assign this letter to the variable best_char.
sally = "sally sells sea shells by the sea shore"
best_char=''
characters={}
for char in sally:
    if char not in characters:
        # we have not seen this character before, so initialize a counter for it
        characters[char] = 0
    #whether we've seen it before or not, increment its counter
    characters[char] += 1
ks=characters.keys()
best_char=ks[0]
for k in ks:
    if characters[k]>characters[best_char]:
        best_char=k
print(best_char)
