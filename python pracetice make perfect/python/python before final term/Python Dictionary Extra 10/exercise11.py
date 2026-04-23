grade_dict = {}
score_dict = {}

for i in range(6):
    print(f"Student @{i+1}")
    print("--- --- --- ---")
    name = input("Enter Your Name : ")
    
    grade = input("Enter Your Grade : ").strip()
    if not grade:
        grade = "N/A"

    score_input = input("Enter Your Score : ").strip()
    if score_input == "":
        score = -1
    else:
        score = int(score_input)

    grade_dict[name] = grade
    score_dict[name] = score
    
profile_dict = {}

for name in set(list(grade_dict.keys()) + list(score_dict.keys())):
    profile_dict[name] = (grade_dict[name], score_dict[name])

for name in profile_dict:
    print(f"{name} -> {profile_dict[name]}")