n = int(input())

found = False
for i in range(1,n+1):
    if i % 7 == 0:
        print(i)
        found = True
        break
if not found:
    print("Not Found")