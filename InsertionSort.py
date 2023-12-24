#WE use concept of SORTED ARRAY SUBSET AND UNSORTED ARRAY SUBSET
#We take TEMP varaibale and insert the FIRST ELEMENT of the UNSORTED SUBSET ARRAY
#O(n2)

arr=[5,4,10,1,6,2]
n=len(arr)

for i in range(1,n):
    temp=arr[i]
    j=i-1
    while j>=0 and arr[j]>temp:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=temp

for i in range(n):
    print(arr[i],end=' ')

