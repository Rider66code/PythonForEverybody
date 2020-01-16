#Challenge: Write a function called beginning that takes a list as input and contains a while loop that only stops once the element of the list is the string ‘bye’. What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. (i.e., if it stops on the 32nd element, the first 10 are returned. If “bye” is the 5th element, the first 4 are returned.) If you want to make this even more of a challenge, do this without slicing
def beginning(chk_list):
    tmp_list=[]
    tmp_val=0
    counter=0
    while (counter<len(chk_list)) and (chk_list[counter]!='bye'):
        tmp_list.append(chk_list[counter])
        counter+=1
        if len(tmp_list)>=10:
            break
    return tmp_list


some_list=['howdy','alright','here i am','and you','what else','stop that','i see','why are you doing that','not me','are you sure','no im not','and why','bye']
print(beginning(some_list))
