#Find the number of lines in the file, travel_plans2.txt, and assign it to the variable num_lines.
fh=open('travel_plans.txt','r')
num_lines=0
txt_lines=fh.readlines()
num_lines=len(txt_lines)
print(num_lines)
