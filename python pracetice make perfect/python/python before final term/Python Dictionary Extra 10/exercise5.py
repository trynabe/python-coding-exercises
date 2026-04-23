grade_dict = {
    "Alice":"A",
    "Bob":"B+",
    "John":"B+",
    "Doe":"F",
    "Nor":"A*"
}
score_dict = {
    "Alice":97,
    "Bob":76,
    "John":79,
    "Doe":27,
    "Nor":999
}
student_tuple_list = []

for name in grade_dict:
    info = (name, grade_dict[name], score_dict[name])
    student_tuple_list.append(info)

for s in student_tuple_list:
    print(s)