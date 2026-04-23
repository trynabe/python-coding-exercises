grade_dict = {
    "Alice":"A",
    "Bob":"B+",
    "John":"B+",
    "Doe":"F",
    "Nor":"A*",
}
passing = {"A","A*","B+","B"}

not_pass_count = 0
for name,grade in grade_dict.items():
    if grade not in passing:
        not_pass_count += 1

print(f"Student Who Did Not Pass : {not_pass_count}")