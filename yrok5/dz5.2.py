a = 0
e = 0
i = 0
o = 0
u = 0
full = 0

print()
str = input()

for j in str:
    if(j == "a"):
        a += 1
        full += 1
    elif(j == "e"):
        e += 1
        full += 1
    elif(j == "i"):
        i += 1
        full += 1
    elif(j == "o"):
        o += 1
        full += 1
    elif(j == "u"):
        u += 1
        full += 1
if a == 0 or e == 0 or i == 0 or o == 0 or u == 0:
    print("False")
else:
    print("Гласных", full)
    print("Согласных", len(str) - full)
