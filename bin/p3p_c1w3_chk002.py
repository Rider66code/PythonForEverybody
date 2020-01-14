sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

# Write your code here.
same_letter_count=0
wordlist=sentence.split()
for word in wordlist:
    if word[-1]==word[0]:
        same_letter_count+=1
print(same_letter_count)
