number = int(input("ENTER NUMBER LIST : "))
count = 0
list_number = []

for i in range(number):
    num = int(input("ENTER NUMBERS INTO LIST : "))
    if num >= 80:
        count += 1
    list_number.append(num)
print(f"SHOW LIST : {list_number}")
print(f"SHOW NUMBERS GREATER THAN 80 : {count}")