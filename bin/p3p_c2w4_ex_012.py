#3. Write a function called str_mult that takes in a required string parameter and an optional integer parameter. The default value for the integer parameter should be 3. The function should return the string multiplied by the integer parameter.
def str_mult(str,val=3):
    mulstr=str*val
    return mulstr

print(str_mult('Hello'))
print(str_mult('Bye',9))
