# 2.3 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking or bad user data.
# 3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.
# This first line is provided for you

hrs = input("Enter Hours:\n")
try:
    float(hrs)
except:
    print("Error, please enter numeric input.")
    quit()
rate = input("Enter Rate:\n")
try:
    float(rate)
except:
    print("Error, please enter numeric input.")
    quit()
if float(hrs)>40:
    pay = 40*float(rate)+(float(hrs)-40)*(float(rate)*1.5)

else:
    pay = float(hrs)*float(rate)

print(pay)
