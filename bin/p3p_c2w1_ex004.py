#Write code to find out how many lines are in the file emotion_words.txt as shown above. Save this value to the variable num_lines. Do not use the len method.
emofile=open("emotion_words.txt", "r")
num_lines=0
for emoline in emofile:
    num_lines+=1
print(num_lines)   
