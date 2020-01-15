#You will need to write two functions for this problem. The first function, divide that takes in any number and returns that same number divided by 2. The second function called sum should take any number, divide it by 2, and add 6. It should return this new number. You should call the divide function within the sum function. Do not worry about decimals.
def divide(dnum):
    drnum=dnum/2
    return drnum

def sum(snum):
    srnum=divide(snum)+6
    return(srnum)

onum=5
print(sum(onum))
