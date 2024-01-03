a1=[[1,2,3],[4,5,6],[7,8,9]]
a2=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]


def RotateImage(a):
    n=len(a)
    res=[[ 0 for j in range(n)]for i in range(n)]
    for i in range(n):
        for j in range(n):
            res[j][n-1-i]=a[i][j]
    for i in range(n):
        for j in range(n):
            print(res[i][j],end=' ')
        print()
     
RotateImage(a1)
print()
RotateImage(a2)

