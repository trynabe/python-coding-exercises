'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab11-count-multiple-letters
*/
'''

# YOUR CODE HERE
'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''
def multiple_letter_count(text):
    d = {}
    for ch in text:
        d[ch] = d.get(ch, 0) + 1
    return d

text = input().strip()
print(multiple_letter_count(text))


