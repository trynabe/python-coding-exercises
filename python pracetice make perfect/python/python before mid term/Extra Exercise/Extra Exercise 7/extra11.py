number = int(input("Order : "))
list_n = []

for i in range(number):
    product = input("Product : ")
    price = int(input("Price : "))
    list_n.append([product,price])

total = 0
for i in range(len(list_n)):
    print(f"{list_n[i][0]} : {list_n[i][1]}")
    total += list_n[i][1]
print(f"Total = {total}")
# Order : 3
# Product : apple      # OUTPUT
# Price : 25           # apple : 25
# Product : milk       # milk : 42
# Price : 42           # bread : 35
# Product : bread      # Total = 102
# Price : 35
