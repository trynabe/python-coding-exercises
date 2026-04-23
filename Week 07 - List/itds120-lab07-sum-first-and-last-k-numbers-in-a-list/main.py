'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab07-sum-first-and-last-k-numbers-in-a-list
 */
'''

# YOUR CODE HERE
list_a = []
k = int(input())

while True:
    s = input()
    if s == "q":
        break
    list_a.append(float(s))

if len(list_a) < k:
    print("Invalid")
else:
    result = sum(list_a[:k]) + sum(list_a[-k:])
    print(result)
