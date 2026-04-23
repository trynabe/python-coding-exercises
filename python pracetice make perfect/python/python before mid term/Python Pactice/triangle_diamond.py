#diamond

number = int(input())

for i in range(number-1):
    for j in range(i,number):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()
for i in range(number):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i,number-1):
        print("*", end=" ")
    for j in range(i,number):
        print("*", end=" ")
    print()