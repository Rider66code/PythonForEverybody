# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)
fname = input("Enter file name:\n ")
try:
    fh = open(fname)
except:
    print("Can't find file " + fname + ", closing.")
    quit()

#bigsname=None
#bigscount=None
#snames=dict()
shours=dict()
for line in fh:
    if not line.startswith("From "):
        continue
    stime=(line.split())[5]
    shour=(stime.split(':'))[0]
    if shour not in shours:
        shours[shour]=1
    else:
        shours[shour]+=1

#print(shours)
#
#for sender in snames:
#    if bigscount is None or bigscount<snames[sender]:
#        bigsname=sender
#        bigscount=snames[sender]
#
#print(bigsname,bigscount)

lhours=list(shours.items())
lhours.sort()

for hour,count in lhours:
    print(hour, count)
