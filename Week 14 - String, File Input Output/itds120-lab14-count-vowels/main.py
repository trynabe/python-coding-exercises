'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab14-count-vowels
*/
'''
# Your Python code goes here
word = input("")
count = {}
vowels = "aeiou"

for i in vowels:
    count[i] = 0

for x in word.lower():
    if x in vowels:
        count[x] += 1

for y in vowels:
    print(f"{y}: {count[y]}")


