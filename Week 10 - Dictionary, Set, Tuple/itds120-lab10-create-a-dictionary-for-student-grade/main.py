'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab10-create-a-dictionary-for-student-grade
*/
'''

# YOUR CODE HERE
student = {}
name = input("")
grade = input("").lower()

if grade == "a":
    student["name"] = name
    student["GRADE"] = grade
else:
    student["name"] = name
    student["grade"] = grade
print(student)