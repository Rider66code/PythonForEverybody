stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
acro=''
acro_so_far=''
sent_list=sent.split()
for word in sent_list:
    if word not in stopwords:
        acro_so_far=acro_so_far+word[0:2].upper()+'. '
acro=acro_so_far[:-2]

print(acro)
