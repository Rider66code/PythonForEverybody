#Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value.
str1 = "peter piper picked a peck of pickled peppers"
freq={}
for char in str1:
    if char not in freq:
        # we have not seen this character before, so initialize a counter for it
        freq[char] = 0
    #whether we've seen it before or not, increment its counter
    freq[char] = freq[char] + 1
print(freq)
