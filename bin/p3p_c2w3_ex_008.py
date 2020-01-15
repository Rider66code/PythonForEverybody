#1. Write a function named total that takes a list of integers as input, and returns the total value of all those integers added together.
def total(x):
    tot=0
    for num in x:
        tot+=num
    return tot

nlist=(1,2,3)
print(total(nlist))
