#Define a function called info with five parameters: name, gender, age, bday_month, and hometown. The function should then return a tuple with all five parameters in that order.
def info(name,gender,age,bday_month,hometown):
    return name,gender,age,bday_month,hometown

myname='John'
mygender='toughguy'
myage=100
mybday_month='September'
myhometown='Las Vegas'
print(info(myname,mygender,myage,mybday_month,myhometown))
