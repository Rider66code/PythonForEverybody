#Write a while loop that is initialized at 0 and stops at 15. If the counter is an even number, append the counter to a list called eve_nums.
eve_nums=[]
counter=0
while (counter<15):
    if counter%2==0:
        eve_nums.append(counter)
    counter+=1
print(eve_nums)
