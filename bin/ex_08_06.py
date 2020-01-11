# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
# Exercise 6: Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers at the end when the user enters “done”. Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes

#largest = None
#smallest = None
vlist=list()
while True:
    num = input("Enter a number:\n")
    if num == "done" :
        break
    try:
        fnum=float(num)
    except:
        print("Invalid input")
        continue
#    if largest is None or largest<fnum:
#        largest=fnum
#    if smallest is None or smallest>fnum:
#        smallest=fnum
    vlist.append(float(num))

#print(vlist)

#print("Maximum:", int(largest))
#print("Minimum:", int(smallest))

print("Maximum:", max(vlist))
print("Minimum:", min(vlist))
