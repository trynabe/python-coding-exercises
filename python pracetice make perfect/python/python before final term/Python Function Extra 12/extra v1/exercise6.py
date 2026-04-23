fruit_dict = {}
number = int(input("จำนวนที่ซื้อ : "))

for i in range(number):
    fruit = input("ผลไม้ : ")
    price = int(input("ราคาผลไม้ : "))
    fruit_dict[fruit] = price

def calc_price(**kwargs):
    total = 0
    for fruit, price in kwargs.items():
        total += price
    return total

print(f"ผลรวมของราคาทั้งหมด = {calc_price(**fruit_dict)}")