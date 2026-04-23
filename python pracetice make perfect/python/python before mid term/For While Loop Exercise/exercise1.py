number = 3

for i in range(1,number+1):
    for j in range(i):
        if j == 0 or j == i - 1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(number-1,0,-1):
    for j in range(i):
        if j == 0 or j == i - 1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()