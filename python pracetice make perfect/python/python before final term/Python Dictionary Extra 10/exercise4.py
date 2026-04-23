# student = {
#     "Alice": {"grade":"A","score":97},
#     "Bob": {"grade":"B+","score":76},
#     "John": {"grade":"B+","score":79},
#     "Doe": {"grade":"F","score":27}
# }
# student.update({
#     "Nor": {"grade":"A*","score":999}
# })

# for name, info in student.items():
#     print(f"{name} has grade {info["grade"]} and {info["score"]}")
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
for name in grade_dict:
    print(f"{name} has grade {grade_dict[name]} and score {score_dict[name]}")