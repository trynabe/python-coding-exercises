'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab03-bubble-tea-order
 */
'''

# YOUR CODE HERE
member = (input())
size = (input())
topping = (input())

price = 50

if (size == "L"):
    price += 10
if (topping == "N"):
    price -= 10
if (member == "Y"):
    price = price * 0.9
print (f"Total price: {price:.1f}")