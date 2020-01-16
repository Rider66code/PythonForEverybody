#Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”).
def sublist(chk_list):
    tmp_list=[]
    tmp_val=0
    counter=0
    while (counter<len(chk_list)) and (chk_list[counter]!='STOP'):
        tmp_list.append(chk_list[counter])
        counter+=1
    return tmp_list

some_list=[1,'STOP',3,4,5]
sublist(some_list)
