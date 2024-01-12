def drawingBook(n,p):
    front=p//2
    back=(n//2)-front
    return min(front,back)

print(drawingBook(6,2))
print(drawingBook(5,4))
