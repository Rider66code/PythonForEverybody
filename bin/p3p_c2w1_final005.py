# Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.
fileref = open("school_prompt.txt", "r")
three=[]
for schoolline in fileref:
    three.append(schoolline.split()[2])
print(three)
fileref.close()
