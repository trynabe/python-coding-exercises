#สามเหลี่ยมครึ่งกลับหัว

number = int(input())

for i in range(1,number+1):
    for j in range(1,i+1):
        print(" ",end=" ")
    for j in range(i,number+1):
        print("*",end=" ")
    for j in range(i,number):
        print("*",end=" ")
    print()