n = int(input("enter the numbers whose sum you want to find - "))
v = 0

for i in range(1,n+1):
    v = v + i
    print(i,"sum =", v)