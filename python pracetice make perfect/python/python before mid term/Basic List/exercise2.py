number = int(input("ENTER NUMBER LIST : "))
list_number = []

for i in range(number):
    num = int(input("ENTER NUMBERS INTO LIST : "))
    list_number.append(num)

list_number.sort()
print(f"SHOW NUMBERS GREATER : {list_number[-1]}")