import math

area_calculator = input("ใส่รูปทรงที่ต้องการคำนวณ(สี่เหลี่ยมผืนผ้า/สี่เหลี่ยมจัตุรัส/วงกลม/สามเหลี่ยม) : ")
if area_calculator == "สี่เหลี่ยมผืนผ้า":
    length = float(input("ใส่ความกว้าง : "))
    width = float(input("ใส่ความยาว : "))
    rectangle = length * width
    print(f"พื้นที่สี่เหลี่ยมผืนผ้า = {round(rectangle,2)}")
elif area_calculator == "สี่เหลี่ยมจัตุรัส":
    width = float(input("ใส่ความยาว"))
    square = width
    print(f"พื้นที่สี่เหลี่ยมจัตุรัส = {round(square,2)}")
elif area_calculator == "วงกลม":
    radius = float(input("ใส่รัศมีวงกลม : "))
    circle = math.pi * radius ** 2
    print(f"พื้นที่วงกลม = {round(circle,2)}")
elif area_calculator == "สามเหลี่ยม":
    height = float(input("ใส่ความสูง : "))
    base_length = float(input("ความยาวฐาน : "))
    triangle = 1/2 * base_length * height
    print(f"พื้นที่สามเหลี่ยม : {round(triangle,2)}")
else:
    print("ไม่รองรับรูปทรงนี้")
