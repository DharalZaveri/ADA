def fact(n):
    fa = 1
    for i in range(1,n+1):
        fa = fa*i
    return fa

a = fact(5)
print(a)