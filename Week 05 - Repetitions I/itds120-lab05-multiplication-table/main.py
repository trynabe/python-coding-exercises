'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab05-multiplication-table
 */
'''

# YOUR CODE HERE
x = int(input())
y = int(input())
i = 1

if y <= 0:
    print("Unable to create a table")
else:
    while i <= y:
        print(f"{x}*{i}={x*i}")
        i += 1