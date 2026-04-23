'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab14-remove-symbol-from-string
*/
'''
# Your Python code goes here
text = input()
clean_text = ""

for ch in text:
    if ch.isalnum():
        clean_text += ch

if clean_text == "":
    print("empty")
else:
    print(clean_text)
