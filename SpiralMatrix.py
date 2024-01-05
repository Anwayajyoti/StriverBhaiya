arr=[[1,2,3],[4,5,6],[7,8,9]]
res=[]
row=len(arr)
col=len(arr[0])
top=0
left=0
right=col-1
bottom=row-1

while len(res)<row*col:
    for i in range(left,right+1):
        res.append(arr[top][i])
    top+=1
    for i in range(top,bottom+1):
        res.append(arr[i][right])
    right-=1
    if (top<=bottom):
        for i in range(right,left-1,-1):
            res.append(arr[bottom][i])
            bottom-=1
    if(left<=right):
        for i in range(bottom,top-1,-1):
                res.append(arr[i][left])
        left+=1
print(res)
