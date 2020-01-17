#Below, we have provided a list of lists named L. Use nested iteration to save every string containing “b” into a new list named b_strings.
L = [['apples', 'bananas', 'oranges', 'blueberries', 'lemons'], ['carrots', 'peas', 'cucumbers', 'green beans'], ['root beer', 'smoothies', 'cranberry juice']]
def list_get(somelist):
    templist=list()
    for sublist in somelist:
        for substring in sublist:
            if 'b' in substring:
                templist.append(substring)
    return templist

b_strings=list_get(L)
print(b_strings)
