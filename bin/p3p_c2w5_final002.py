#Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered positive words. Use the list, positive_words to determine what words will count as positive. The function should return a positive integer - how many occurrences there are of positive words in the text. Note that all of the words in positive_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
positive_words = []

def strip_punctuation(someword):
    for char in punctuation_chars:
        someword=someword.replace(char, '')
    dpword=someword
    return dpword

with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(somesent):
    tmpcount=0
    tmplist=somesent.split()
    for word in tmplist:
        if strip_punctuation(word).lower() in positive_words:
            tmpcount+=1
    return tmpcount


print(get_pos("Hello There"))
