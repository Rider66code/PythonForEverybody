#Write a function called decision that takes a string as input, and then checks the number of characters. If it has over 17 characters, return “This is a long string”, if it is shorter or has 17 characters, return “This is a short string”.
def decision(s):
    tmp_val=0
    for char in s:
        tmp_val+=1
    if tmp_val>17:
        return 'This is a long string'
    elif tmp_val<=17:
        return 'This is a short string'

x='Who ever is going to read such a long and boring string which being used only for comparison no matter how long you can make it and do not underestimate the limits of your monitor to read such a long and boring line.'
printer=decision(x)
print(printer)
