total = 0

while True:
    number = (input(""))
    if number == "q":
        break
    number = int(number)
    total += number
print(f"{total}")