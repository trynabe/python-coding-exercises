x = [[10,2,3,4],[1,9,3,4],[1,2,8,4],[1,2,3,7]]
n = len(x)
total = 0

for i in range(n):
    total = total + x[i][i]
print(total)