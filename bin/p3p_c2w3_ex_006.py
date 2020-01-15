#Write a function called s_change that takes one string as input and returns that string, concatenated with the string ” for fun.”.
def s_change(s):
    newstr='{} for fun.'.format(s)
    return newstr

str='Now I\'m here doing some strange stuff'
x=s_change(str)
print(x)
