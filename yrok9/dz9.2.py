a = set()
b = set()

n = int(input("Введите колличество символов в первом списке: "))
for i in range(n):
    a.add(int(input()))

m = int(input("Введите колличество символов во втором списке: "))
for i in range(m):
    b.add(int(input()))

print(len(a.intersection(b)))