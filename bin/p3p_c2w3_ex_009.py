#2. Write a function called count that takes a list of numbers as input and returns a count of the number of elements in the list.
def count(x):
    cnum=0
    for num in x:
        cnum+=1
    return cnum

nlist=(1,2,3)
print(count(nlist))
