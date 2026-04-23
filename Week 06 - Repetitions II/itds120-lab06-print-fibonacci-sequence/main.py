'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab06-print-fibonacci-sequence
 */
'''

# YOUR CODE HERE
x = int(input())

f0 = 0
f1 = 1
a = 1

for i in range(x):
    f2 = f0 + f1
    print(f"{f0}" , end=" ")
    f0 = f1
    f1 = f2
    if a % 5 == 0:
        print()
    a += 1
    