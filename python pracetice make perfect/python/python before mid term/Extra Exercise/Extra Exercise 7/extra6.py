n = 10
number = []

for i in range(1,n+1):
    number.append(i)
for n in number:
    if n % 2 == 0:
        print(n,end=" ")
#OUTPUT
# 2 4 6 8 10