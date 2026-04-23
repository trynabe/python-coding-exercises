'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab06-print-a-triangle-of-stars
 */
'''

# YOUR CODE HERE
m = int(input())

for i in range(1, m + 1):
    for j in range(m - i):
        print("-", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    for j in range(m - i):
        print("-", end="")
    print()