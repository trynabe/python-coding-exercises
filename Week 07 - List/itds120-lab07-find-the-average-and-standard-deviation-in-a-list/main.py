'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab07-find-the-average-and-standard-deviation-in-a-list
 */
'''

# YOUR CODE HERE
number = []

while True:
    s = input()
    if s == "q":
        break
    number.append(float(s))

total = 0
for i in number:
    total += i
mean = total / len(number)

sum_square = 0
for n in number:
    sum_square += (n - mean) ** 2
std = (sum_square / (len(number) - 1)) ** 0.5

print(round(mean, 2), round(std, 2))
