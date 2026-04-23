'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab02-calculate-slope-of-line
 */
'''

# YOUR CODE HERE
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

sol = (y2 - y1)/(x2 - x1)

print(f"This slope is {round(sol,2)}")