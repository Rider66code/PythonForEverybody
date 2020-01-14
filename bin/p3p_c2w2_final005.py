#Create a dictionary called wrd_d from the string sent, so that the key is a word and the value is how many times you have seen that word.
sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
wordlist=sent.split()
wrd_d={}
for word in wordlist:
    if word not in wrd_d:
        # we have not seen this character before, so initialize a counter for it
        wrd_d[word] = 0
    #whether we've seen it before or not, increment its counter
    wrd_d[word] += 1
print(wrd_d)
