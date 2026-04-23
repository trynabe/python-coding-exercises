# student_tuple = []

# for i in range(6):
#     name = input("Enter Your Name : ")
#     grade = input("Enter Your Grade : ")
#     score = int(input("Enter Your Score : "))
#     student_tuple.append((name, grade, score))

# grade_order = ["A*", "A", "B+", "B", "C", "D", "F"]

# print("Avg by grade:")
# for g in grade_order:
#     scores = [x[2] for x in student_tuple if x[1] == g]
#     if scores:
#         ave = sum(scores) / len(scores)
#         print(f"{g} : {ave:.2f}")

# print("Top by grade:")
# for g in grade_order:
#     students_in_grade = [x for x in student_tuple if x[1] == g]
#     if students_in_grade:
#         top_student = max(students_in_grade, key=lambda x: x[2])
#         print(f"{g} : {top_student[0]}({top_student[2]})")

student_tuples = [
    ("Alice","A",97),
    ("Nor","A*",95),
    ("Nina","A",90),
    ("Bob","B+",92),
    ("Max","B",91),
    ("John","B+",89)
]
grades = {}  # key = เกรด, value = list ของ (name, score)

for student in student_tuples:
    name = student[0]
    grade = student[1]
    score = student[2]
    
    if grade not in grades:
        grades[grade] = []
    grades[grade].append((name, score))

print("Avg by grade:")
for grade in grades:
    scores = []
    for student in grades[grade]:
        scores.append(student[1])
    avg = sum(scores) / len(scores)
    print(grade, ":", round(avg, 2))

print("Top by grade:")
for grade in grades:
    top_score = 0
    top_name = ""
    for student in grades[grade]:
        if student[1] > top_score:
            top_score = student[1]
            top_name = student[0]
    print(grade, ":", top_name + "(" + str(top_score) + ")")