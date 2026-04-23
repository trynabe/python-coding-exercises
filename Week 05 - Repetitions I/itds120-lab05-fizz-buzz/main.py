'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab05-fizz-buzz
 */
'''

# YOUR CODE HERE
while True:    
    n = int(input())
    if n > 0:
        break
    else:
        print("")
i = 1
while i <= n:
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
    i += 1