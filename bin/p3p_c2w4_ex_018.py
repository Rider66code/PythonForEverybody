#Write a function, test, that takes in three parameters: a required integer, an optional boolean whose default value is True, and an optional dictionary, called dict1, whose default value is {2:3, 4:5, 6:8}. If the boolean parameter is True, the function should test to see if the integer is a key in the dictionary. The value of that key should then be returned. If the boolean parameter is False, return the boolean value “False”.
def test(sint, sbool=True,dict1={2:3, 4:5, 6:8}):
    sresult=False
    if sbool==True:
        for pairs in dict1.items():
            if int(pairs[0])==sint:
                sresult=int(pairs[1])
    return sresult

print(test(4))
