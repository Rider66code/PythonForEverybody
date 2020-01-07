#Exercise 5: Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the
#converted temperature.
tcel = input("Enter Temperature in Celsius:\n")
try:
    float(tcel)
except:
    print("Bad value entered, quitting.")
    quit()
tfahr=(float(tcel)*(9/5))+float(32)
print("Fahrenheit temperature according to input is:",tfahr)
