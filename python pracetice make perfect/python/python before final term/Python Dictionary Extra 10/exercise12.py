grade_dict = {}
score_dict = {}

student_max = 3

for i in range(6):
    print(f"Student @{i+1}")
    print("--- --- --- ---")
    name = input("Enter Your Name : ")
    grade = input("Enter Your Grade : ")
    score = int(input("Enter Your Score : "))

    grade_dict[name] = grade
    score_dict[name] = score

student = []
for name in grade_dict:
    student.append((name, grade_dict[name], score_dict[name]))

grade_weight = {"A*":7,"A":6,"B+":5,"B":4,"C":3,"D":2,"F":1}

sorted_student = sorted(student,key=lambda x: (x[2], grade_weight[x[1]]),reverse=True)

for i in range(min(student_max, len(sorted_student))):
    name, grade, score = sorted_student[i]
    print(name,grade,score)
