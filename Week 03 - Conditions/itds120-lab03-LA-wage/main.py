'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab03-LA-wage
 */
'''

# YOUR CODE HERE
time = int(input())
hour = 50

if time <= 40:
    result1 = hour * time
    print(result1)
elif time >= 40:
    result2 = 2000 + (time - 40) * 75
    print(result2)