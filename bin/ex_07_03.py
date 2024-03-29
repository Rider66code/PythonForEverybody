#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
# Use the file name mbox-short.txt as the file name
#fname = input("Enter file name: ")
#fh = open(fname)
#for line in fh:
#    if not line.startswith("X-DSPAM-Confidence:") : continue
#    print(line)
#print("Done")
# Exercise 3: Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to their program. Modify the program that prompts the user for the file name so that it prints a funny message when the user types in the exact file name “na na boo boo”. The program should behave normally for all other files which exist and don’t exist. Here is a sample execution of the program:
fname = input("Enter file name:\n")
if fname == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    quit()
try:
    fh = open(fname)
except:
    print("Can't find file " + fname + ", closing.")
    quit()
lcount=0
ltotal=None
lval=None
lavg=None
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    lcount=lcount+1
    lval=float(line[line.find(':')+1:].strip())
    if ltotal is None:
        ltotal=lval
    else:
        ltotal=ltotal+lval

lavg=ltotal/lcount
print("Average spam confidence:",lavg)
