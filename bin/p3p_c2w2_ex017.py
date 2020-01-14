#Provided is a string saved to the variable name sentence. Split the string into a list of words, then create a dictionary that contains each word and the number of times it occurs. Save this dictionary to the variable name word_counts.
sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."
word_counts={}
word_list=sentence.split()
for word in word_list:
    if word not in word_counts:
        # we have not seen this word before, so initialize a counter for it
        word_counts[word] = 0

    #whether we've seen it before or not, increment its counter
    word_counts[word] = word_counts[word] + 1

for word in word_counts.keys():
    print(word + ": " + str(word_counts[word]) + " occurrences")
