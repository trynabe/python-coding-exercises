n = 2
m = 3

matrix = []
for i in range(n):
    row_list = []
    for j in range(m):
        x = int(input())
        row_list.append(x)
    matrix.append(row_list)

flat_list = []
for row in matrix:
    for x in row:
        flat_list.append(x)

flat_list.sort()
print(flat_list)