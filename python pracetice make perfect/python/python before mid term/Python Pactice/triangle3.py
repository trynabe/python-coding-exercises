#สามเหลี่ยมครึ่งด้านบนฝั่งซ้าย

number = int(input())

for i in range(number):
    for j in range(i, number):
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()