A = []
for i in range(2):
    row_list = []
    for j in range(2):
        x = int(input())
        row_list.append(x)
    A.append(row_list)

B = []
for i in range(2):
    row_list = []
    for j in range(2):
        x = int(input())
        row_list.append(x)
    B.append(row_list)

C = [[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        for k in range(2):
            C[i][j] += A[i][k] * B[k][j]

for row_list in C:
    print(*row_list)