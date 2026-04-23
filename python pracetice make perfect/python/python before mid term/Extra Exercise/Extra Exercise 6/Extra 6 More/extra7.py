number = 5

for i in range(1,number+1):
    for j in range(1,i+1):
        if i == 1 or i == number or j == 1 or j == i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()