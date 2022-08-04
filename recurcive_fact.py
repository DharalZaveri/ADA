def factorial(n):
    f = 1
    if n==0 or n==1: return 1
    else:
        return(n*factorial(n-1))

a = factorial(6)
print(a)