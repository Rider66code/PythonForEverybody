#Create a class called NumberSet that accepts 2 integers as input, and defines two instance variables: num1 and num2, which hold each of the input integers. Then, create an instance of NumberSet where its num1 is 6 and its num2 is 10. Save this instance to a variable t.
class NumberSet:
    """NumberSet Class for accepting two integers as input for two instance variables num1 and num2"""
    def __init__(self,putA,putB):
        self.num1=putA
        self.num2=putB

t = NumberSet(6,10)
