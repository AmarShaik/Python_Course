# A function is a reusable block of code that performs a specific task.
# You define a function once and can call (use) it as many times as you want.


def calculateGmean(a, b):
    mean = (a * b) / (a + b)
    print(mean)

def isGreater(a, b):
    if (a > b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")

def isLesser(a, b):
    pass
a = 9
b = 8
isGreater(a, b)
calculateGmean(a, b)
# gmean1 = (a*b)/(a+b)
# print(gmean1)
c = 8
d = 74
isGreater(c, d)
calculateGmean(c, d)
# gmean2 = (c*d)/(c+d)
# print(gmean2)