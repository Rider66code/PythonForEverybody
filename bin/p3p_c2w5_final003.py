#Next, copy in your strip_punctuation function and define a function called get_neg which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered negative words. Use the list, negative_words to determine what words will count as negative. The function should return a positive integer - how many occurrences there are of negative words in the text. Note that all of the words in negative_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

negative_words = []

def strip_punctuation(someword):
    for char in punctuation_chars:
        someword=someword.replace(char, '')
    dpword=someword
    return dpword

def get_pos(somesent):
    tmpcount=0
    tmplist=somesent.split()
    for word in tmplist:
        if strip_punctuation(word).lower() in positive_words:
            tmpcount+=1
    return tmpcount

def get_neg(somesent2):
    tmpcount=0
    tmplist=somesent2.split()
    for word in tmplist:
        if strip_punctuation(word).lower() in negative_words:
            tmpcount+=1
    return tmpcount


with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
