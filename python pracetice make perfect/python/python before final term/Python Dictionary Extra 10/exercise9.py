score_dict = {
    "Alice":97,
    "Bob":76,
    "John":79,
    "Doe":27,
    "Nor":999
}
enrolled = {
    "Alice",
    "Bob",
    "John",
    "Doe",
    "Nor",
    "Sara"
}

for name in enrolled:
    if name not in score_dict:
        print(f"คนที่ไม่มีคะแนน : {name}")