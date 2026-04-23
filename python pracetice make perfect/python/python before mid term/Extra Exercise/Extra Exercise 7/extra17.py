n = 3
m = 4

matrix = []
for i in range(n):
    row_list = []
    for j in range(m):
        x = int(input())
        row_list.append(x)
    matrix.append(row_list)

for j in range(m):
    col_max = max(matrix[i][j] for i in range(n))
    print(col_max, end=" ")
