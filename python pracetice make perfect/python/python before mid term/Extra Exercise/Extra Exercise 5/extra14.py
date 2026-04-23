produce = int(input("กรอกราคารวมสินค้า: "))
pay = int(input("กรอกจำนวนเงินที่จ่าย: "))

change = pay - produce
print(f"เงินทอนทั้งหมด: {change}")

money = [1000,500,100,50,20,10,5,1]

for d in money:
    count = change // d
    change = change % d
    if d >= 20:
        print(f"แบงค์ {d} : {count} ใบ")
    else:
        print(f"เหรียญ {d} : {count} เหรียญ")
