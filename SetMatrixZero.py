a=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print('Initial Matrix: ')
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=' ')
    print()
print()

row=set()
col=set()

for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j]==0:
            row.add(i)
            col.add(j)

for i in range(len(a)):
    for j in range(len(a[i])):
        if i in row or j in col:
            a[i][j]=0

print('Resultant Matrix: ')
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=' ')
    print()
print()


