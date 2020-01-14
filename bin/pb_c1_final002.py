stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
acro=''
org = "The organization for health, safety, and education"
org_list=org.split()
for word in org_list:
    if word not in stopwords:
        acro=acro+word[0].upper()
print(acro)
