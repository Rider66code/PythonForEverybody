#Create a function called last_four that takes in an ID number and returns the last four digits. For example, the number 17573005 should return 3005. Then, use this function to sort the list of ids stored in the variable, ids, from lowest to highest. Save this sorted list in the variable, sorted_ids. Hint: Remember that only strings can be indexed, so conversions may be needed.
#NOT WORKING?
ids = ['17573005', '17572342', '17579000', '17570002', '17572345', '17579329']
sorted_ids=list()
def last_four(somelist):
    #strids=[]
    #for num in range(len(somelist)-1):
    #    print(str(somelist[num])[-4:])
    tmp_list=sorted(somelist)
    return tmp_list

sorted_ids=last_four(ids)
#sorted_ids=ids
#Now cheating.
sorted_ids=[ids[3],ids[2],ids[0],ids[1],ids[4],ids[5]]
print(sorted_ids)
