term = int(input("ค่าเทอม : "))
max = int(input("ค่าเทอมที่มากที่สุด : "))

while True:
    term += term * 5/100
    print(term)
    if term > max:
        break
    