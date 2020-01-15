#The list below, tuples_lst, is a list of tuples. Create a list of the second elements of each tuple and assign this list to the variable country.
country=[]
tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ('Rio', 'Brazil', 2016, 'Current'), ('Tokyo', 'Japan', 2020, 'Future')]
for info in tuples_lst:
    country.append(info[1])
print(country)
