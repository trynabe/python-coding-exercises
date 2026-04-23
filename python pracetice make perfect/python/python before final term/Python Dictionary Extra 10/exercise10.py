grade_dict = {
    "Alice": "A",
    "Bob": "B+",
    "John": "B+",
    "Doe": "F",
    "Nor": "A*",
    "Nina": "A",
    "Mark": "B"
}

grade_count = {}

for info in grade_dict.values():
    grade_count[info] = grade_count.get(info, 0) + 1

order = ["A", "A*", "B", "B+", "F"]

for grade in order:
    if grade in grade_count:
        print(f"{grade} : {grade_count[grade]}")