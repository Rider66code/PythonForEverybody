#Define a function called info with the following required parameters: name, age, birth_year, year_in_college, and hometown. The function should return a tuple that contains all the inputted information.
def info(name,age,birth_year,year_in_college,hometown):
    return name,age,birth_year,year_in_college,hometown

myname='John Doe'
myage=65
mybirth=1900
myyearincollege=1918
myhometown='Atlanta'

print(info(myname,myage,mybirth,myyearincollege,myhometown))
