'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab07-remove-vowels-from-the-list
 */
'''

# YOUR CODE HERE
letter = []

while True:
    s = input()
    if s == "0":
        break
    letter.append(s)
vowels = "aeiou"
for i in vowels:
    while i in letter:
        letter.remove(i)
print(letter)
