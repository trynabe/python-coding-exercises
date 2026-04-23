#result infinity

total = 0

while True:
    num = int(input("Take A Number : "))
    if num <= 0:
        break
    total += num
print(f"Result = {total}")