'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab11-multiply-even-number-functions
*/
'''

# YOUR CODE HERE
'''
Example of Function Uses:
multiply_even_numbers([2,3,4,5,6]) # 48
'''
list_number = []
num = int(input(""))

for i in range(num):
    number = int(input(""))
    list_number.append(number)

def multiply(list_number):
    total = 1
    for num in list_number:
        if num % 2 == 0:
            total = total * num
    if num % 2 != 0:
        total = -1
    return total
print(multiply(list_number))
