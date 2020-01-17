#Provided is a nested data structure. Follow the instructions in the comments below. Do not hard code.

nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}

# Check to see if the string data is a key in nested, if it is, assign True to the variable data, otherwise assign False.
data=None
twentyfour=None
whole=None
physics=None
for keyval in nested:
    if type(keyval) is str:
        data=True
        print(data)
    if keyval=='data':
        for subdata in keyval:
            if subdata==24:
                twentyfour=True
                print(twentyfour)
                break
            else:
                twentyfour=False
    if keyval=='window':
        if 'whole' not in keyval:
            whole=False
        else:
            whole=True
    if keyval=='physics':
        physics=True
    else:
        physics=False
# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.

# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.

# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.
