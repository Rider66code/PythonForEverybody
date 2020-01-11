# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
# Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

largest = None
smallest = None
count = 0
snum=0
while True:
    num = input("Enter a number:\n")
    if num == "done" :
        break
    try:
        fnum=int(num)
    except:
        print("Invalid input")
        continue
    count=count+1
    snum=snum+int(num)
    if largest is None or largest<fnum:
        largest=fnum
    if smallest is None or smallest>fnum:
        smallest=fnum

avnum=snum/count
print("Sum is", int(snum))
print("Maximum is", int(largest))
print("Minimum is", int(smallest))
print("Average is", float(avnum))
