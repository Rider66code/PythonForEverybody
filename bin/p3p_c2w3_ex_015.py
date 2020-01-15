#Write a function, length, that takes in a list as the input. If the length of the list is greater than or equal to 5, return “Longer than 5”. If the length is less than 5, return “Less than 5”.
def length(ilst):
    rstr=''
    cnt=0
    if len(ilst)>=5:
        rstr='Longer than 5'
    else:
        rstr='Less than 5'
    return rstr

elst=([])
print(length(elst))
