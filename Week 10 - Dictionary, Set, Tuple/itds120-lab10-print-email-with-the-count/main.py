'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab10-print-email-with-the-count
*/
'''

# YOUR CODE HERE
number = int(input(""))
mail_dict = {}

for i in range(number):
    mail = input("")
    message = int(input(""))
    if message % 2 == 0:
        mail_dict[mail] = message
    
if len(mail_dict) == 0:
    print("Not Found")
else:
    for mail in mail_dict:
        print(mail)
