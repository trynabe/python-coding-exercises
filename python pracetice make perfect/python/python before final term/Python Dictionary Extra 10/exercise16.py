possible_grade = {
    "A*","A","B+","B","C","D","F"
}
grade_dict = {
    "Alice":"A",
    "Bob":"B+",
    "John":"B+",
    "Doe":"F",
    "Nor":"A*",
    "Nina":"A",
    "Max":"B",
    "Weird":"E"
}

invalid = {grade_dict[key] for key in grade_dict if grade_dict[key] not in possible_grade}
print(f"Invalid grades in data : {invalid}")

used_grades = set(grade_dict.values())
unused = possible_grade - used_grades
print(f"Unused possible grades: {unused}")