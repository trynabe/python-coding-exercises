'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab12-sum-even-numbers-in-the-list
*/
'''

# YOUR CODE HERE

#----   function   ----#
n = int(input())
number_list = []

for i in range(n):
    number = int(input())
    number_list.append(number)
    
def sum_even_number(*number_list):
    total = 0
    for number in number_list:
        if number % 2 == 0:
            total = total + number
    return total

result = sum_even_number(*number_list)
print(result)