str = input()
result = "yes"

for i in range(0, len(str) // 2):
    if str[i] != str[-(i + 1)]:
        result = "no"
        break

print(result)
