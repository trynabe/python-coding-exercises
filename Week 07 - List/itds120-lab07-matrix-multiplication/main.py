'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab07-matrix-multiplication
 */
'''

# YOUR CODE HERE
n = int(input())

A = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    A.append(row)

B = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    B.append(row)

C = []
for i in range(n):
    row = []
    for j in range(n):
        total = 0
        for k in range(n):
            total += A[i][k] * B[k][j]
        row.append(total)
    C.append(row)

print(A)
print(B)
print(C)
