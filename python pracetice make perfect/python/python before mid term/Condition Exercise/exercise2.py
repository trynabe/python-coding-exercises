year = int(input("ใส่ปี : "))
if year % 4 != 0:
    print(f"{year} is not a Leap Year")
elif year % 4 == 0:
    print(f"{year} is a Leap Year")
elif year % 100 != 0:
    print(f"{year} is a Leap Year")
elif year % 400 != 0:
    print(f"{year} is not a Lear Year")
elif year % 100 != 0:
    print(f"{year} is Leap Year")