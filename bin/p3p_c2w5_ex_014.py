#Sort the list ids by the last four digits of each id. Do this using lambda and not using a defined function. Save this sorted list in the variable sorted_id.
tmp_val=str()
tmp_dict=dict()
sorted_id=list()
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
for num in range(len(ids)):
    tmp_val=str(ids[num])[-4:]
    tmp_dict[ids[num]]=tmp_val
#print(tmp_dict)
for orig_num,num in sorted(tmp_dict.items(),key=lambda fnum:fnum[1]):
    sorted_id.append(orig_num)
