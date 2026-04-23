total = 0
count = 0

while True:
    number = int(input())
    if number < 0:
        break
    if number > 0:
        total += number
        count += 1

if count == 0:
    print("ไม่มีจำนวนเต็มบวกให้คำนวณ")
else:
    average = total / count
    print(f"ค่าเฉลี่ยของจำนวนเต็มบวก = {average}")