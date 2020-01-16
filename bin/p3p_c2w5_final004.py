#Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv which has the fake generated twitter data (the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet). Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. Copy the code from the code windows above, and put that in the top of this code window. Now, you will write code to create a csv file called resulting_data.csv, which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet. The file should have those headers in that order. Remember that there is another component to this project. You will upload the csv file to Excel or Google Sheets and produce a graph of the Net Score vs Number of Retweets. Check Coursera for that portion of the assignment, if you’re accessing this textbook from Coursera.

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(someword):
    for char in punctuation_chars:
        someword=someword.replace(char, '')
    dpword=someword
    return dpword

def get_pos(somesent):
    tmpcount=0
    tmplist=somesent.split()
    for word in tmplist:
        if strip_punctuation(word).lower() in positive_words:
            tmpcount+=1
    return tmpcount

def get_neg(somesent2):
    tmpcount=0
    tmplist=somesent2.split()
    for word in tmplist:
        if strip_punctuation(word).lower() in negative_words:
            tmpcount+=1
    return tmpcount

twitterfile = open("project_twitter_data.csv", 'r')
lines = twitterfile.readlines()
twitterfile.close()
header = lines[0]
field_names = header.strip().split(',')
#To be removed below
print(field_names)
#print(len(lines[1:]))
resultdata=open("resulting_data.csv","w")
resultdata.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n")
for row in lines[1:]:
    t_retweets=0
    t_replies=0
    t_ps=0
    t_ns=0
    t_net=0
    t_row=str()
    t_list=[t_retweets,t_replies,t_ps,t_ns,t_net]
    tmp_row_list=row.strip().split(',')
    t_list[0]=tmp_row_list[1]
    t_list[1]=tmp_row_list[2]
    t_list[2]=get_pos(tmp_row_list[0])
    t_list[3]=get_neg(tmp_row_list[0])
    t_list[4]=t_list[2]-t_list[3]
    t_row=(','.join(str(num) for num in t_list))+'\n'
    resultdata.write(t_row)
resultdata.close()
