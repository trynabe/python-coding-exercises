n = 3

a = []
for i in range(n):
    row = []
    for j in range(n):
        x = int(input())
        row.append(x)
    a.append(row)

for j in range(n):
    print(a[-1][j], a[-2][j], a[0][j])