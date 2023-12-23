#TAKES MINIMUM AND SWAPS
#O(n2)

#>[13,46,24,52,20,9]
#>[9,46,24,52,20,13]
#>[9,13,24,52,20,46]
#>[9,13,20,52,24,46]
#>[9,13,20,24,52,46]
#>[9,13,20,24,46,52]

#Takes n-1 Steps

#CODE:
arr=[13,46,24,52,20,9]
n =len(arr)

for i in range(n):
    mini=i
    for j in range(i+1,n):
        if arr[j]<arr[mini]:
            mini=j
    arr[mini],arr[i]=arr[i],arr[mini]

for i in range(n):
    print(arr[i],end=' ')