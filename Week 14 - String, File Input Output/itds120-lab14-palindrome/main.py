'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab14-palindrome
*/
'''
# Your Python code goes here
text = input().lower()
cleanned = ""

for ch in text:
    if ch.isalpha():
        cleanned += ch

if cleanned == cleanned[::-1]:
    print("palindrome")
else:
    print("not palindrome")
