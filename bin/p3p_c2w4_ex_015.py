#Create a function called mult that has two parameters, the first is required and should be an integer, the second is an optional parameter that can either be a number or a string but whose default is 6. The function should return the first parameter multiplied by the second.
def mult(num,sattr=6):
    mul_num=num*sattr
    return mul_num

print(mult(5))
