#Write a function called stop_at_four that iterates through a list of numbers. Using a while loop, append each number to a new list until the number 4 appears. The function should return the new list.
def stop_at_four(limit_num):
    tmp_list=[]
    tmp_val=0
    counter=0
    while (counter<len(limit_num)) and (limit_num[counter]!=4):
        tmp_list.append(limit_num[counter])
        counter+=1
    return tmp_list

val_list=[1,6,2,3,9]
print(stop_at_four(val_list))
