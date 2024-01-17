arr=[3,2,4]
n=len(arr)
target=6
hash={}
for i in range(n):
    res=target-arr[i]
    if res in hash:
        print(hash[res],i)
    else:
        hash[arr[i]]=i
    
