# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
# Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.
def scorecalc(s):
    if s<0 or s>1:
        print("Score is out of range, stopping.")
    elif s>=0.9:
        print("A")
    elif s>=0.8:
        print("B")
    elif s>=0.7:
        print("C")
    elif s>=0.6:
        print("D")
    else:
        print("F")

score = input("Enter Score:\n")
try:
    fscore=float(score)
except:
    print("Cannot parse score, stopping.")
    quit()

scorecalc(float(score))
