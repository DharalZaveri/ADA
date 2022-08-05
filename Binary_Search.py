def Binary(arr,l,n,x):
    if n>= 1:
        mid = l+(n-1)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return Binary(arr,l,n-1,x)
        elif arr[mid]<x:
            return Binary(arr,l,n+1,x)
        
a = [2,4,6,8,23,33,45,78]
x = 33
y = Binary(a,0,len(a)-1,x)
print(y)