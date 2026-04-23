while True:
    x = int(input("ENTER A NUMBER (X) : "))
    if x > 0:
        break
while True:
    y = int(input("ENTER A NUMBER (Y) : "))
    if y > 0:
        break
for i in range(1,x+1):
    print(f"MULTIPLE TABLE OF {i} IN RANGE {y}")
    for j in range(1,y+1):
        print(f"{i}*{j} = {i*j}")