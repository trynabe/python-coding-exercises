number = int(input("ENTER A NUMBER : "))
print("TL = 1,TL = 2,TL = 3,TL = 4")
direction_id = int(input("ENTER A DIRECTION ID : "))
pattern = input("ENTER A PATTERN : ")

if direction_id == 1:
    for i in range(number,0,-1):
        for j in range(i):
            print(f"{pattern}",end=" ")
        print()

if direction_id == 2:
    for i in range(number):
        for j in range(i+1):
            print(" ",end=" ")
        for j in range(i,number):
            print(f"{pattern}",end=" ")
        print()

if direction_id == 3:
    for i in range(number+1):
        for j in range(i):
            print(f"{pattern}",end=" ")
        print()

if direction_id == 4:
    for i in range(number):
        for j in range(i,number):
            print(" ",end=" ")
        for j in range(i+1):
            print(f"{pattern}",end=" ")
        print()
