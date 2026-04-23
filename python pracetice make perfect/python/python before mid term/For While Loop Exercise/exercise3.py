total = 0
count = 0
while True:
    number = int(input())
    if number > 0 and number % 2 == 0:
        total += number
        count += 1
        if count == 4:
            break
print(total)