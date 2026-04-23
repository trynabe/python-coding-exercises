'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab10-create-tuple-dictionary
*/
'''

# YOUR CODE HERE
number = int(input(""))
student_dict = {}

for i in range(number):
    firstname = input("")
    lastname = input("")
    score = float(input(""))
    student_dict[(firstname, lastname)] = score

max_value = max(student_dict.values())

for key, value in student_dict.items():
    if value == max_value:
        firstname, lastname = key
        print(f"Firstname: {firstname}, Last name: {lastname}")
        break