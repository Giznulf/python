result = 0
x = int(input())
for i in range(1, int(x ** 0.5) + 1):
    if x % i == 0:
        result += 1
    if i != (x // i):
        result += 1

print("Kоличество натуральных делителей числа", x, "равен", result)
