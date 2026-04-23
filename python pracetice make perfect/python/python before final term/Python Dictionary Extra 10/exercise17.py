grade_dict = {
    "Alice":"A",
    "Bob":"B+",
    "John":"B+",
    "Doe":"F",
    "Nor":"A*",
    "Nina":"A",
    "Max":"B"
}
score_dict = {
    "Alice":97,
    "Bob":92,
    "John":92,
    "Doe":27,
    "Nor":95,
    "Nina":90
}
possible_grade = {"A*","A","B+","B","C","D","F"}
passing = {"A*","A","B+","B"}

student_data = []
for name, score in score_dict.items():
    if name in grade_dict:
        grade = grade_dict[name]
        passed_status = grade in passing

        student_tuple = (name, grade, score, passed_status)
        student_data.append(student_tuple)
        

grade_weights = {"A*":0,"A":1,"B+":2,"B":3,"C":4,"D":5,"F":6}

sorted_student = sorted(student_data, key=lambda s:(not s[3], -s[2],grade_weights[s[1]],s[0]))

print("Ranking:")

for name,grade,score,passed_status in sorted_student:
    if passed_status == True:
        status = "PASS"
    else:
        status = "FAIL"
    print(f"{name} {grade} {score} {status}")

print("Summary:")

passed_count = 0
failed_count = 0
for student in sorted_student:
    if student in sorted_student:
        if student[3] == True:
            passed_count += 1
        else:
            failed_count += 1
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")

top_3_list = []
for student in sorted_student:
    if student[3] == True:
        top_3_list.append(student[0])
    if len(top_3_list) == 3:
        break
print(f"Top-3 passed: {top_3_list}")

used_grade = set(grade_dict.values())
unused_grade = possible_grade - used_grade
print(f"Unused grade: {unused_grade}")
