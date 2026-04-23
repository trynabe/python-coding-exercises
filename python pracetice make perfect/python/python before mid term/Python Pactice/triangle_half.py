#สามเหลี่ยมครึ่ง

number = int(input())

for i in range(number):
    for j in range(i,number):
        print(" ", end=" ")
    for j in range(i):
        print("*", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()