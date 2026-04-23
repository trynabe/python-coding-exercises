x = [[1,2,3],[4,5,6],[7,8,9]]
row = len(x)
for i in range(row):
    col = len(x[i])
    for j in range(col):
        print(x[i][j],end=" ")
    print()