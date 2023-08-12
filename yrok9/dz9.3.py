nums = list(map(int, input().split()))
x = set()

for i in range(len(nums)):
    a = len(x)
    x.add(nums[i])
    b = len(x)
    if b > a:
        print("NO")
    else:
        print("YES")