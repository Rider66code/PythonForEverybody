#The dictionary travel contains the number of countries within each continent that Jackie has traveled to. Find the total number of countries that Jackie has been to, and save this number to the variable name total. Do not hard code this!
total=0
travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}
for country in travel:
    total=total+travel[country]
print(total)
