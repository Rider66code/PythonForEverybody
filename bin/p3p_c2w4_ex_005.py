#Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).
def sublist(limit_num):
    tmp_list=[]
    tmp_val=0
    counter=0
    while (counter<len(limit_num)) and (limit_num[counter]!=5):
        tmp_list.append(limit_num[counter])
        counter+=1
    return tmp_list

some_list=[1,2,3,4,5]
sublist(some_list)
