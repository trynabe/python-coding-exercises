count = 1
list_str = []
for i in range(3):
    s = input("input letter : ")
    if s in list_str:
        count += 1
    list_str.append(s)
if count == 1:
    print("ควย")
else:
    print(count)