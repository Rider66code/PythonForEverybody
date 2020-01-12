# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)
# Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary. After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.
fname = input("Enter file name:\n")
try:
    fh = open(fname)
except:
    print("Can't find file " + fname + ", closing.")
    quit()

snlist=list()
snames=dict()
for line in fh:
    if not line.startswith("From "):
        continue
    sname=(line.split())[1]
    if sname not in snames:
        snames[sname]=1
    else:
        snames[sname]+=1

for name,count in snames.items():
    snlist.append((count,name))

snlist.sort(reverse=True)
topname=snlist.pop(0)
tcount,tname=topname
print(tname,tcount)
