#Input: a = [1, 2, 3, 2], n = 4
#Output: 2 3
#Explanation: 
#a[ 2 ] = 3 is greater than a[ 3 ]. Hence it is a Superior Element. 
#a[ 3 ] = 2 is the last element. Hence it is a Superior Element.
#The final answer is in sorted order.

a=[1,2,3,2]
def superiorElements(a):
    # Write your code here.
    n=len(a)
    res=[]
    maxi=a[n-1]
    res.append(maxi)
    for i in range(n-2,-1,-1):
        if a[i]>maxi:
            res.append(a[i])
            maxi=max(a[i],maxi)
    return res
print (superiorElements(a))
