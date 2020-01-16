#Sort the following list by each element’s second letter a to z. Do so by using lambda. Assign the resulting value to the variable lambda_sort.
lambda_sort=list()
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
for word in sorted(ex_lst,key=lambda wstr:wstr[1]):
    lambda_sort.append(word)
print(lambda_sort)
