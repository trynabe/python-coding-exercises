score_dict = {
    "Alice":97,
    "Bob":76,
    "John":79,
    "Doe":27,
    "Nor":999
}

student = []
for name in score_dict:
    info = (name,score_dict[name])
    student.append(info)

for s in student:
    print(s)

max_value = max(score_dict.values())
print("Max Value : "+str(max_value))

for key,value in score_dict.items():
    if value == max_value:
        print("Name (Max) : "+key)