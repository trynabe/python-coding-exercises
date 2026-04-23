'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab07-count-the-number-of-character-occurrences
 */
'''

# YOUR CODE HERE
input_list = []

while True:
    s = input()
    if s == "-1":
        break
    input_list.append(s)

input_list.sort()
word = []

for i in range(len(input_list)):
    s = input_list[i]
    if s not in word:
        count = 0
        for j in range(len(input_list)):
            if input_list[j] == s:
                count += 1
        print(f"{s}={count}",end=" ")
        word.append(s)

