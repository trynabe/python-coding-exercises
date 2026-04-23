# score = []
# for i in range(3):
#     row = []
#     for j in range(2):
#         x = int(input(f"Student {i+1} Subject {j+1} : "))
#         row.append(x)
#     score.append(row)

# for i in range(len(score)):
#     total = sum(score[i])
#     print(f"Student {i+1} total = {total}")

score = []
for i in range(3):
    a = []
    for j in range(2):
        x = int(input(f"คนที่ {i+1} ใส่คะแนน : "))
        a.append(x)
    score.append(a)
    
for i in range(len(score)):
    total = sum(score[i])
    print(f"Student {i+1} total = {total}")
# คนที่ 1 ใส่คะแนน : 80
# คนที่ 1 ใส่คะแนน : 75
# คนที่ 2 ใส่คะแนน : 90
# คนที่ 2 ใส่คะแนน : 60
# คนที่ 3 ใส่คะแนน : 70
# คนที่ 3 ใส่คะแนน : 85
# Student 1 total = 155
# Student 2 total = 150
# Student 3 total = 155