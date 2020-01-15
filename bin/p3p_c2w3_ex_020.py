#5. Below, we have provided a list of tuples. Write a for loop that saves the second element of each tuple into a list called seconds.
seconds=[]
tups = [('a', 'b', 'c'), (8, 7, 6, 5), ('blue', 'green', 'yellow', 'orange', 'red'), (5.6, 9.99, 2.5, 8.2), ('squirrel', 'chipmunk')]
for element in tups:
    seconds.append(element[1])
print(seconds)
