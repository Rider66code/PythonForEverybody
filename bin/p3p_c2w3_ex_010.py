#1. Write two functions, one called addit and one called mult. addit takes one number as an input and adds 5. mult takes one number as an input, and multiplies that input by whatever is returned by addit, and then returns the result.
def addit(num):
    addint=num+5
    return addint

def mult(ornum):
    mulint=ornum*addit(ornum)
    return mulint

print(mult(5))
