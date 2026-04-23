#round 1-5 = result

total = 0
for i in range(1,6):
    number = int(input("Round "+ str(i)+" : "))
    total += number
print(f"Result = {total}")
print("End")