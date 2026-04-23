'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab03-quadrant-and-coordinate
 */
'''

# YOUR CODE HERE
x = float(input())
y = float(input())

if x == 0 or y == 0:
    print("Undetermined quadrant")
elif x >= 0 and y >= 0:
    print("Q1")
elif x <= 0 and y >= 0:
    print("Q2")
elif x <= 0 and y <= 0:
    print("Q3")
elif x >= 0 and y <= 0:
    print("Q4")