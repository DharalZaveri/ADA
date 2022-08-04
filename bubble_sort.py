def bubble_sort(ar):
    for i in range(len(ar)):
        for j in range(0,len(ar)-1):
            if ar[j]>ar[j+1]:
                temp = ar[j]
                ar[j] = ar[j+1]
                ar[j+1] = temp


arr = [2,6,3,1,7]
bubble_sort(arr)
print(arr)
