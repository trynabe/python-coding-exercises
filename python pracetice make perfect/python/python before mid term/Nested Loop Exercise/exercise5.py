while True:
    number = int(input("ENTER A NUMBER : "))
    if number > 0 and number <= 6:
        break
for i in range(1,number+1):
    for j in range(number-i):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    for j in range(i-1,0,-1):
        print("*",end="")
    print()