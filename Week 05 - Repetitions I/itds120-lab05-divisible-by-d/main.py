'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab05-divisible-by-d
 */
'''

# YOUR CODE HERE
x = int(input())
y = int(input())
d = int(input())
count = 0

for i in range(x ,y+1):
    if i % d == 0:
        print(i, end = " ")
        count += 1
print(f"count={count}")