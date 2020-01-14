f = open('scarlet.txt', 'r')
txt_lines = f.readlines()
# now txt_lines is a list, where each item is one
# line of text from the story
print(len(txt_lines))
print(txt_lines[70:85])
