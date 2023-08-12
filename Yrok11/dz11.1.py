import math
def fact(x):
    y = math.factorial(x)
    res = []
    for i in range(y, 1, -1):
        res.append(math.factorial(i))
    return res

print(fact(int(input())))