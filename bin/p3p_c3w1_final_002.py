#Below, a list of lists is provided. Use in and not in tests to create variables with Boolean values. See comments for further instructions.

lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]

#Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
yellow=None
if 'yellow' in lst[2]:
    yellow=True
else:
    four=False
print(yellow)

#Test to see if 4 is in the second list of lst. Save to variable ``four``
four=None
if 4 in lst[1]:
    four=True
else:
    four=False
print(four)


#Test to see if 'orange' is in the first element of lst. Save to variable ``orange``
orange=None
if 'orange' in lst[0]:
    orange=True
else:
    orange=False
print(orange)
