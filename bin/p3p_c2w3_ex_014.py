#Write a function, accum, that takes a list of integers as input and returns the sum of those integers.
def accum(ilst):
    tot=0
    for iint in ilst:
        tot+=iint
    return(tot)

alst=(1,2,3)
print(accum(alst))
