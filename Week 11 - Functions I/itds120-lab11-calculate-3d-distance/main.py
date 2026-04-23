'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab11-calculate-3d-distance
*/
'''

# YOUR CODE HERE
'''
Example of Function Uses:
cal_dist(x1,y1,z1,x2,y2,z2)
'''
import math

def cal_dist(x1=7.0, y1=4.0, z1=3.0, x2=17.0, y2=6.0, z2=2.0):
    dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
    return round(dist, 2)

x1 = input()
y1 = input()
z1 = input()
x2 = input()
y2 = input()
z2 = input()

if 'q' in [x1, y1, z1]:
    x1, y1, z1 = 7.0, 4.0, 3.0
else:
    x1, y1, z1 = float(x1), float(y1), float(z1)

if 'q' in [x2, y2, z2]:
    x2, y2, z2 = 17.0, 6.0, 2.0
else:
    x2, y2, z2 = float(x2), float(y2), float(z2)

print(cal_dist(x1, y1, z1, x2, y2, z2))

