#Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once the element of the list is the number 7. What is returned is a list of all of the numbers up until it reaches 7.
def check_nums(chk_list):
    tmp_list=[]
    tmp_val=0
    counter=0
    while (counter<len(chk_list)) and (chk_list[counter]!=7):
        tmp_list.append(chk_list[counter])
        counter+=1
    return tmp_list

some_list=[1,2,3,4,5]
check_nums(some_list)
