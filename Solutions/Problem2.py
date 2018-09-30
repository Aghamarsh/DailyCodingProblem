def divisor(a,b):
    temp = 0

    while a >= b :
        temp = temp + 1
        a = a - b

    return temp

l=list((map(int, input().split())))
ans=[]
product = 1

for i in range(0,len(l)):
    product = product * l[i]

for i in range(0,len(l)):
    ans.append(divisor(product,l[i]))

print(ans)
