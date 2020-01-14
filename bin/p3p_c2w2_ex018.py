# Create a dictionary called char_d from the string stri, so that the key is a character and the value is how many times it occurs.
stri = "what can I do"
char_d={}
for char in stri:
    if char not in char_d:
        char_d[char]=0
    char_d[char]=char_d[char]+1
for char in char_d.keys():
    print(char+": "+str(char_d[char])+" occurences")
