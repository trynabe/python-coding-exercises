total = 0
while True:
    number = int(input())
    if number < 0:
        continue
    if number == 0:
        break
    total += 1
print(f"Count of positives = {total}")