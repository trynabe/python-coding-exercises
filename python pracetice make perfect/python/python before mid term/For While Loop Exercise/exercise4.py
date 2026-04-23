number = int(input("ใส่เลขซะไอควาย : "))

for i in range(1,number+1):
    if i % 7 == 0 or i % 10 == 7:
        print("seven-up")
        continue
    print(i)