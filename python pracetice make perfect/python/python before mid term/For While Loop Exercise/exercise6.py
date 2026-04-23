print("=== ร้านขายผลไม้ ===")
print("ราคาต่อกิโลกรัม")
print("กล้วย = 30 บาท, แอปเปิ้ล = 50 บาท, ส้ม = 40 บาท")

while True:
    print("คุณจะซื้อผลไม้กี่ชนิด : ",end=" ")
    number = int(input(""))
    if number > 0:
        break

total = 0
for fruits in range(number):
    print("กรอกชื่อผลไม้",end=" ")
    fruits = input("")
    if fruits == "Banana":
        print("กรอกน้ำหนัก (กก.) : ",end=" ")
        kilo = int(input())
        total += kilo * 30
    if fruits == "Apple":
        print("กรอกน้ำหนัก (กก.) : ",end=" ")
        kilo = int(input())
        total += kilo * 50
    if fruits == "Orange":
        print("กรอกน้ำหนัก (กก.) : ",end=" ")
        kilo = int(input())
        total += kilo * 40
print("=== สรุปการซื้อ ===")
print("ราคารวมก่อนลด "+ str(total))
if total > 200:
    print("ส่วนลดหรือค่าบริการ : "+ str(total * 0.1))
    total -= total * 0.1
elif total < 100:
    total += 20
    print("ส่วนลดหรือค่าบริการ : "+ str(20))

print("ราคาสุทธิที่ต้องจ่าย : "+ str(total))

