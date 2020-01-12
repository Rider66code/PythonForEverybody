# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)
# Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.
fname = input("Enter file name:\n")
try:
    fh = open(fname)
except:
    print("Can't find file " + fname + ", closing.")
    quit()

#bigsname=None
#bigscount=None
snames=dict()
for line in fh:
    if not line.startswith("From "):
        continue
    sname=(line.split())[1]
    if sname not in snames:
        snames[sname]=1
    else:
        snames[sname]+=1

#for sender in snames:
#    if bigscount is None or bigscount<snames[sender]:
#        bigsname=sender
#        bigscount=snames[sender]

print(snames)
#print(bigsname,bigscount)
