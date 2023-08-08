X = int(input())

A = int(input())
B = int(input())

if A >= X or B >= X:
    if A >= X and B >= X:
        print(2)
    elif A >= X:
        print("Mike")
    else:
        print("Ivan")
elif (A + B) >= X:
    print(1)
else:
    print(0)