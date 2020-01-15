#Define a function called information that takes as input, the variables name, birth_year, fav_color, and hometown. It should return a tuple of these variables in this order.
def information(name,birth_year,fav_color,hometown):
    return (name,birth_year,fav_color,hometown)

myname='John Doe'
mybirth=1900
myfavcolor='Black'
myhometown='Atlanta'
print(information(myname,mybirth,myfavcolor,myhometown))
