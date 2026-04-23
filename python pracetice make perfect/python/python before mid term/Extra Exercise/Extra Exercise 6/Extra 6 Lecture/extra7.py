n = int(input())
s = int(input())
    
total = 0
for i in range(1,n+1):
    if i % 2 != 0:
        continue
    if total + i > s:
        break
    print(i,end=" ")
    total += i