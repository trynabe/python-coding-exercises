number = 5

for i in range(1,number+1):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i-1,number):
        print("*",end=" ")
    for j in range(i,number):
        print("*",end=" ")
    print()