#Write a function called stop_at_z that iterates through a list of strings. Using a while loop, append each string to a new list until the string that appears is “z”. The function should return the new list.

def stop_at_z(chk_list):
    tmp_list=[]
    tmp_val=0
    counter=0
    while (counter<len(chk_list)) and (chk_list[counter]!='z'):
        print(chk_list[counter][:1].lower())
        tmp_list.append(chk_list[counter])
        counter+=1
    return tmp_list

some_list=['STOP','auto','naff4','lolz','bro']
print(stop_at_z(some_list))
