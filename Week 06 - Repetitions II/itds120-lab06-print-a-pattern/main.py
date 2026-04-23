'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab06-print-a-pattern
 */
'''

# YOUR CODE HERE
while True:
    n = int(input())
    if n <= 1 or n % 2 == 0:
        continue
    else:
        break
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or j == i or j + i == n-1:
            print("*" , end =" ")
        else:
            print("-" , end =" ")
    print()
