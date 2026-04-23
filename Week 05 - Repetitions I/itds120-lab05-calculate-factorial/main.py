'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab05-calculate-factorial
 */
'''

# YOUR CODE HERE
x = int(input(""))

result = 1

if x == 0:
    print(1)
elif x == 1:
    print(1)
else:
    for i in range(x, 0, -1):
        print(i, end="")
        if i > 1:
            print("*", end="")
        result *= i
    print(f"={result}")

