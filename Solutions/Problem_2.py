def divisor(a, b):
    temp = 0

    while a >= b:
        temp = temp + 1
        a = a - b

    return temp


l = list((map(int, input().split())))
ans = []
product = 1

zcount = 0

for i in range(0, len(l)):
    if l[i] == 0:
        zcount = zcount + 1
    else:
        product = product * l[i]

if zcount == 0:
    for i in range(0, len(l)):
        ans.append(divisor(product, l[i]))
elif zcount == 1:
    for i in range(0, len(l)):
        if l[i] == 0:
            ans.append(divisor(product, l[i]))
        else:
            ans.append(0)
else:
    for i in range(0, len(l)):
        ans.append(0)

print(ans)
