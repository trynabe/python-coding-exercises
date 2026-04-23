'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab06-print-a-triangle-of-numbers
 */
'''

# YOUR CODE HERE
while True:
    n = int(input())
    if n > 0:
        break
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()

