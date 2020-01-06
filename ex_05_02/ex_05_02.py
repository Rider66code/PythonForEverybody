# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.


largest = None
smallest = None
while True:
    num = input("Enter a number:\n")
    if num == "done" :
        break
    try:
        fnum=float(num)
    except:
        print("Invalid input")
    if largest is None or largest<fnum:
        largest=fnum
    if smallest is None or smallest>fnum:
        smallest=fnum

print("Maximum is", int(largest))
print("Minimum is", int(smallest))
