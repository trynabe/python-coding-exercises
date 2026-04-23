number = int(input())

total = 0
for i in range(1,number+1):
    if i % 5 == 0:
        continue
    total += i
print(f"Sum = {total}")