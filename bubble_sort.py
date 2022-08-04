def bubble_sort(ar):
    for i in range(len(ar)):
        for j in range(0,len(ar)-1):
            if ar[j]>ar[j+1]:
                temp = ar[j]
                ar[j] = ar[j+1]
                ar[j+1] = temp


ar = []
for i in range(0,9):
    a = int(input("Enter Numbers for bubble_sort: "))
    ar.append(a)
print("Befor Bubble_sort ",ar)
arr = [2,6,3,1,7]
bubble_sort(ar)
print(f"After Bubble_sort{ ar}")
