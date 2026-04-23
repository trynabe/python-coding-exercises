'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab12-remove-negative-numbers-from-the-list
*/
'''

# YOUR CODE HERE

#----   function   ----#
n = int(input())
number_list = []

for i in range(n):
    number = int(input())
    number_list.append(number)
    
def remove_negative(number_list):
    positive_list = list(filter(lambda x: x >= 0, number_list))
    return positive_list

result = remove_negative(number_list)

print(result)