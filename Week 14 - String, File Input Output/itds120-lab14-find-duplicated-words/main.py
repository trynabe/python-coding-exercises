'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab14-find-duplicated-words/main.py
*/
'''
# Your Python code goes here
word = input().split(" ")
word_list = {}
found = False

for w in word:
    w = w.strip(".,“”\"")
    if w:
        if w in word_list:
            word_list[w] += 1
        else:
            word_list[w] = 1

for key, value in word_list.items():
    if value > 1:
        print(f"{key}: {value}")
        found = True

if not found:
    print("no duplicated word")