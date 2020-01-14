# Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
fileref = open("school_prompt.txt", "r")
p_words=[]
for line in fileref:
    linelist=line.split()
    for word in linelist:
        if 'p' in word:
            p_words.append(word)
print(p_words)
fileref.close()
