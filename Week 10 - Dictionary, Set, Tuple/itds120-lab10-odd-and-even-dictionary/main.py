'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab10-odd-and-even-dictionary
*/
'''

# YOUR CODE HERE
number = int(input(""))
number_dict = {}

for i in range(number):
    num = int(input(""))
    if num % 2 == 0:
        number_dict[num] = "even"
    else:
        number_dict[num] = "odd"

print(number_dict)