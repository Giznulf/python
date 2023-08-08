A = int(input())
B = int(input())

result = ""

for i in range(A, B + 1):
    if (i % 2) == 0:
        result += (" " + str(i)) 
print(result)