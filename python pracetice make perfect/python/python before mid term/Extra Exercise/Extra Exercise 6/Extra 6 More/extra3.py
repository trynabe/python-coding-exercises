number = 5

for i in range(number,0,-1):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,number+1):
        print("*",end=" ")
    for j in range(i-1,number-1):
        print("*",end=" ")
    print()