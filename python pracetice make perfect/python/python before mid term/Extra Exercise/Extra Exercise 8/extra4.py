people = []

number = int(input("จำนวนคน : "))

for i in range(number):
    name = str(input("ชื่อ : "))
    weight = float(input("น้ำหนัก (กิโลกรัม) : "))
    height = float(input("ส่วนสูง (เมตร) : "))

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        cat = "Underweight"
    elif bmi < 25:
        cat = "Normal"
    elif bmi < 30:
        cat = "Overweight"
    else:
        cat = "Obese"


    people.append(name)
    people.append([bmi, cat])

print(people,end=" ")