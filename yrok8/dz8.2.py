n = int(input())
res = list(map(int, input().split()))
res.insert(0, res.pop(-1))
print(res)