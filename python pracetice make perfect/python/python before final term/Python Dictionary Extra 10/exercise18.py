raw_data = [
    ("Alice", "A", 97),
    ("Bob", "B+", 76),
    ("John", "B+", 79),
    ("Doe", "F", 27),
    ("Nor", "A*", 92),
    ("Alice", "A", 95)
]
student_info = {}
dropped_duplicates = set()

for name, grade, score in raw_data:
    if name not in student_info:
        student_info[name] = (grade, score)
    else:
        if score > student_info[name][1]:
            student_info[name] = (grade, score)
        dropped_duplicates.add(name)

sorted_students = sorted(student_info.items())

final_list = [(i+1, name, grade, score)
for i, (name, (grade, score))in enumerate(sorted_students)]

print("Rows:")
for row in final_list:
    print(row)

print("Dropped duplicates:", dropped_duplicates)
