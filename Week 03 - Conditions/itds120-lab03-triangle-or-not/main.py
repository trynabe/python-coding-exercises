'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab03-triangle-or-not
 */
'''

# YOUR CODE HERE
a = float(input())
b = float(input())
c = float(input())

if a <= 0 or b <= 0 or c <= 0:
    print("Invalid triangle")
elif (a + b > c) and (a + c > b) and (b + c > a):
    print("Valid triangle")
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Invalid triangle")