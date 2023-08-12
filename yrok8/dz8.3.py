m = int(input())
n = int(input())
passengers = []
for i in range(n):
    passengers.append(int(input()))
passengers.sort(reverse=True)

boats = 0
i = 0
while i < n:
    if passengers[i] + passengers[i + 1] <= m and i + 1 < n:
        i += 2
    else:
        i += 1
    boats += 1

print(boats)