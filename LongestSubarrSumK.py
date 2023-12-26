a1=[1,2,3,1,1,1,1]
k1=3

a2=[1,2,1,3]
k2=2

a3=[2,2,4,1,2]
k3=2

def LongestSubArr(a,k):
    n=len(a)
    l=0
    for i in range(n):
        for j in range(i,n):
            s=0
            for K in range(i,j+1):
                s+=a[K]
            if s==k:
                l=max(l,j-i+1)
    return l
                    
                
    

print(LongestSubArr(a1,k1))
print(LongestSubArr(a2,k2))
print(LongestSubArr(a3,k3))


                
        
