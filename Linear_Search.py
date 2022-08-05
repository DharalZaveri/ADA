def Linear(arr,n):
    for i in range(1,len(arr)+1):
        if (arr[i]==i):
            return i
        
arr  = []
for i in range(0,5):
    inp = int(input(""))
    arr.append(inp)
a = Linear(arr,20)
print(a,11)