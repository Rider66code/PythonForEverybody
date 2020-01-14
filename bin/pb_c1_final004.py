p_phrase = "was it a car or a cat I saw"
r_phrase = ''
chars_list=[]
for char in p_phrase:
    chars_list.append(char)
chars_list.reverse()
r_phrase = r_phrase.join(chars_list)
print(r_phrase)
