#Write code to find out how many lines are in the file emotion_words.txt as shown above. Save this value to the variable num_lines. Do not use the len method.
fh=open('emotion_words.txt','r')
num_lines=0
txt_lines=fh.readlines()
for line in txt_lines:
    num_lines+=1
print(num_lines)
