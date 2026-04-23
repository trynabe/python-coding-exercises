n = 4
m = 4
t = 6

for i in range(1,n+1):
    for j in range(1,m+1):
        if i == j:
            continue
        if  i*j > t:
            break
        print(f"({i},{j})",end=" ")