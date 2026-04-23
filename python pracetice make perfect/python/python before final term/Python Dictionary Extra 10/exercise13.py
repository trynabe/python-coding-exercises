# grade_dict = {}
# score_dict = {}

# for i in range(7):
#     print(f"Student @{i+1}")
#     print("--- --- --- ---")
#     name = input("Enter Your Name : ")
#     grade = input("Enter Your Grade : ")
#     score = int(input("Enter Your Score : "))
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
    "John":89,
    "Doe":27,
    "Nor":95,
    "Nina":90,
    "Max":91
}

# grade_dict[name] = grade
# score_dict[name] = score

student_tuple_list = []

for name in grade_dict:
    info = (name , grade_dict[name], score_dict[name])
    if info[2] >= 90 and info[1] != "F":
        student_tuple_list.append(info)

sorted_student = sorted(student_tuple_list, key=lambda x: x[2], reverse=True)
print(sorted_student)