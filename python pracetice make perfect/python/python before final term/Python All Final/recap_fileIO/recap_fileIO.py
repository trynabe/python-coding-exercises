import numpy as np
students = {}
with open("input1.txt","r") as f:
    lines = f.readlines()
    header = lines[0].strip().split(",")
    subject = header[1:]

    for line in lines[1:]:
        parts = line.strip().split(",")
        name = parts[0]
        scores = list(map(int,parts[1:]))
        students[name] = scores

totals = {}
print("\nStudent totals:")
for name, scores in students.items():
    total = sum(scores)
    totals[name] = total
    print(f"{name} : {total}")

all_scores = np.array(list(students.values()))
subject_avgs = np.mean(all_scores,axis=0)

print("\nSubject average:")
for i,subj in enumerate(subject):
    print(f"{subj} : {subject_avgs[i]:.2f}")

with open("output1.txt","w") as f:
    f.write("Student Total:\n")
    for name , total in totals.items():
        f.write(f"{name} : {total}\n")
    f.write("\nSubject averages:\n")
    for i , subj in enumerate(subject):
        f.write(f"{subj} : {subject_avgs[i]:.2f}\n")
print("\nReport saved to report.txt")