'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab05-average-score
 */
'''

# YOUR CODE HERE
total = 0
count = 0

while True:
    s = input()
    if s == "q":
        break
    score = int(s)
    if score >= 0 and score <= 100:
        total = total + score
        count = count + 1
average = round(total / count, 2)

if average >= 50:
    print(average, "Satisfactory")
else:
    print(average, "Unsatisfactory")

