number = 4

student_list = []
for i in range(number):
    student = input(f"Student {i+1} : ")
    grade = input(f"Student Grade {i+1} : ")
    student_list.append([student,grade])

for i in range(len(student_list)):
    if student_list[i][1] == "A":
        print(student_list[i][0])

# INPUT         OUTPUT
#    4          Ann
#    Ann A      Cat
#    Bob B+
#    Cat A
#    Don C