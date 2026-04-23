number = 5

for i in range(1,number+1):
    for j in range(number-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        if i == number or j == 0 or j == 2*i - 2:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()