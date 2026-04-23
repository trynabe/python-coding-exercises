all_student = {
    "6501":{"name":"livid",
        "major":"it",
        "gpa": 4.00},
    "6502":{
        "name":"vegas",
        "major":"cs",
        "gpa": 3.88}
}
student_name = all_student["6502"]["name"]
student_grade = all_student["6502"]["gpa"]
print(f"Student : {student_name}, Grade : {student_grade}")