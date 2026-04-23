while True:
    number = int(input("ENTER A NUMBER : "))
    if number > 0:
        break

for i in range(number):
    for j in range(number):
        if (i == j or i == number-1
            or i == 0 or i == number-1
            or j == 0 or j == number-1
            or i == j
            or i + j == number-1):
            print("*",end=" ")
        else:
            print("-",end=" ")
    print()