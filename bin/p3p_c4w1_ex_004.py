#Create a class called Animal that accepts two numbers as inputs and assigns them respectively to two instance variables: arms and legs. Create an instance method called limbs that, when called, returns the total number of limbs the animal has. To the variable name spider, assign an instance of Animal that has 4 arms and 4 legs. Call the limbs method on the spider instance and save the result to the variable name spidlimbs.
class Animal:
    """Animal testing class"""
    def __init__(self,initArms,initLegs):
        self.arms=initArms
        self.legs=initLegs

    def limbs(self):
        return self.arms+self.legs

spider=Animal(4,4)
spidlimbs=spider.limbs()
