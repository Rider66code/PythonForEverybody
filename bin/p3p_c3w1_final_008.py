#Iterate through the contents of l_of_l and assign the third element of sublist to a new list called third.

l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]
third=list()
for el in l_of_l:
    #print(l_of_l.index(el))
    #print(l_of_l[1])
    for subel in el:
        if l_of_l[l_of_l.index(el)].index(subel)==2:
            #print('Yes')
            third.append(l_of_l[l_of_l.index(el)][2])
            #print(l_of_l[l_of_l.index(el)][l_of_l[l_of_l.index(el)][l_of_l[l_of_l.index(el)].index(subel)]])
        #third.append(l_of_l[l_of_l.index(el)][2])
print(third)
