arr=[13,46,24,52,20,9]
n= len(arr)

for i in range(n):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

for i in range(n):
    print(arr[i],end=' ')
