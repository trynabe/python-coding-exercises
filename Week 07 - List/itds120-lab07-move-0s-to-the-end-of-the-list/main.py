'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab07-move-0s-to-the-end-of-the-list
 */
'''

# YOUR CODE HERE
number = []

for i in range(10):
    num = int(input())
    number.append(num)

result = []

for n in number:
    if n != 0:
        result.append(n)

for n in number:
    if n == 0:
        result.append(n)
print(result)