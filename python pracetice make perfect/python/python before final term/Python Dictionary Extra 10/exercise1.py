student = {}

for i in range(4):
    print(f"Student @{i+1}")
    name = input("Enter Your Name : ")
    grade = input("Enter Your Grade : ")
    score = int(input("Enter Your Score : "))
    student[name] = {"grade": grade , "score": score}

print("--- Grade List ---")
for name, info in student.items():
    print(f"| {name} | {info['grade']} |")

print("--- Score List ---")
for name, info in student.items():
    print(f"| {name} | {info['score']} |")

# student[name] = {"grade": grade, "score":score}
# for name, info in student.items():
#     print(f"{name} | {info['grade']} | {info['score']}")