#Write a function called change that takes any string, adds “Nice to meet you!” to the end of the argument given, and returns that new string.
def change(istr):
    nstr=istr+'Nice to meet you!'
    return nstr

astr='Hello kid,'
print(change(astr))
