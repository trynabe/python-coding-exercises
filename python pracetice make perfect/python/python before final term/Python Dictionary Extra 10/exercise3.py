student = {
    "Alice": {"grade":"A","score":97},
    "Bob": {"grade":"B+","score":76},
    "John": {"grade":"B+","score":79},
    "Doe": {"grade":"F","score":27}
}
student.update({
    "Nor": {"grade":"A*","score":999}
})

for name, info in student.items():
    print(f"{name} | {info["grade"]} | {info["score"]}")