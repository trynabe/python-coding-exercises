'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab10-create-a-shopping-cart-list-of-dictionaries
*/
'''

# YOUR CODE HERE
shopping_list = []
number = int(input(""))

for i in range(number):
    name = input()
    quantity = int(input())
    price = float(input())
    shopping_list.append({"name":name, "quantity":quantity, "price":price})

result = 0
for item in shopping_list:
    result += item["quantity"] * item["price"]

print(shopping_list)
print(result)