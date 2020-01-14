s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
# Write your code here.
num_vowels=0
wordlist=s.split()
vowels = ['a','e','i','o','u']
for word in wordlist:
    #print(word)
    for char in word:
        #print(char)
        if char in vowels:
            num_vowels+=1
print(num_vowels)
