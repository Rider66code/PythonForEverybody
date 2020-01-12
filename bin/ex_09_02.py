# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)
# Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.
# Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).
fname = input("Enter file name:\n")
try:
    fh = open(fname)
except:
    print("Can't find file " + fname + ", closing.")
    quit()

#bigsname=None
#bigscount=None
sdays=dict()
for line in fh:
    if not line.startswith("From "):
        continue
    sday=(line.split())[2]
    if sday not in sdays:
        sdays[sday]=1
    else:
        sdays[sday]+=1

#for sender in snames:
#    if bigscount is None or bigscount<snames[sender]:
#        bigsname=sender
#        bigscount=snames[sender]

print(sdays)
#print(bigsname,bigscount)
