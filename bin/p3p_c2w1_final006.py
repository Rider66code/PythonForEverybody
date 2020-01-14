# Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.
fileref = open("emotion_words.txt", "r")
emotions=[]
for emoline in fileref:
    emotions.append(emoline.split()[0])
print(emotions)
fileref.close()
