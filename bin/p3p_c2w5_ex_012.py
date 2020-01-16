#We have provided the dictionary groceries. You should return a list of its keys, but they should be sorted by their values, from highest to lowest. Save the new list as most_needed.
groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
def shoplist(somedict):
    tmplist=[]
    counter=0
    for stock,count in sorted(somedict.items(),key=lambda stat:stat[1],reverse=True):
        counter+=1
        tmplist.append(stock)
    return tmplist
most_needed=shoplist(groceries)
