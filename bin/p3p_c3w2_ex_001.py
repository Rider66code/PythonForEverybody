#1. Using map, create a list assigned to the variable greeting_doubled that doubles each element in the list lst.
lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
greeting_doubled=map((lambda value: 2*value),lst)
print(greeting_doubled)
