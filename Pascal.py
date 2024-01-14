rows=int(input('Rows: '))

def pascal(rows):
    if rows==0:
        return []
    if rows==1:
        return [[1]]
        
    prevRow=pascal(rows-1)
    newRow=[1]*rows

    for i in range(1,rows-1):
        newRow[i]=prevRow[-1][i-1]+prevRow[-1][i]

    prevRow.append(newRow)
    return prevRow

print( pascal(rows))