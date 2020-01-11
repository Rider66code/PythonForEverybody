# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)
# Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.
fname = input("Enter file name:\n ")
try:
    fh = open(fname)
except:
    print("Can't find file " + fname + ", closing.")
    quit()

charlist=list()
schars=dict()
for line in fh:
    lline=line.lower()
    for lchar in lline:
        if lchar.isalpha():
            if lchar not in schars:
                schars[lchar]=1
            else:
                schars[lchar]+=1

for lchar,count in schars.items():
    charlist.append((count,lchar))

charlist.sort(reverse=True)

for count,lchar in charlist:
    print(lchar,count)
