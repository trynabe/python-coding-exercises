while True:
    number = int(input("ENTER A NUMBER : "))
    if number > 0:
        break

for i in range(number):
    for j in range(number):
        if i == j:
            print("o",end=" ")
        elif (i + j) % 2 == 0:
            print("+",end=" ")
        else:
            print("-",end=" ")
    print()