# break / continue

for i in range(1,13):
    if i == 5:
        continue
    if i % 2 == 0:
        continue
    if i == 11:
        break
    print(i)
print("end")