'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab06-find-prime-numbers
 */
'''

# YOUR CODE HERE
while True:
    num = int(input())
    if num == 1000:
        continue
    elif num <= 1:
        continue
    else:
        break

total = 0
for i in range(2, num + 1):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=" ")
        total += 1
        
print()
print(f"Total prime numbers: {total}")

