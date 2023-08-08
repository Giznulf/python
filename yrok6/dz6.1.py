result = 0
N = int(input())

for i in range(N):
    x = int(input())
    if x == 0:
        result += 1

print("Нолей", result)
