#Create a dictionary, freq_words, that contains each word in string str1 as the key and its frequency as the value.
str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
wordlist=str1.split()
freq_words={}
for word in wordlist:
    if word not in freq_words:
        # we have not seen this character before, so initialize a counter for it
        freq_words[word] = 0
    #whether we've seen it before or not, increment its counter
    freq_words[word] += 1
print(freq_words)
