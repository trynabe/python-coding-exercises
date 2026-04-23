Which statement about file modes is TRUE?
Select the best answer.
✔ B. 'w' opens a file for writing only, creating it if it doesn't exist. It truncates existing contents.

Open & Read

1. Read entire contents:
with open("input.txt", "r", encoding="utf-8")as f:
    data = f.read()
print(data)
f.close()

2. Read one line:
with open("input.txt", "r", encoding="utf-8")as f:
    line = f.readline()
print(line)
f.close()

3. Read all lines into a list:
with open("input.txt", "r", encoding="utf-8")as f:
    lines = f.readlines()
print(lines)
f.close()

4. Iterate safely over lines (preferred pattern):
with open("input.txt", "r", encoding="utf-8")as f:
    for line in f:
        pass
    print(line,end="")

Multiple choice
Which lines correctly write text to a file?
✔ B. with open("out.txt","w",encoding="utf-8") as f: f.write("hi\n")
✔ C. with open("out.txt","a",encoding="utf-8") as f: f.write("next\n")

1. Write a single line:
with open("out.txt","w",encoding="utf-8")as f:
    f.write("Hello, World!\n")

2. Write multiple lines using a loop:
lines = ["A","B","C"]
with open("out.txt","w",encoding="utf-8")as f:
    for line in lines:
        f.write(line)
        f.write("\n")

Debugging Writing One Word Per Line
words = ["apple", "banana", "cherry"]
with open("words.txt","w")as f:
    for w in words:
        f.write(w)
        f.write("\n")

Debugging File I/O
with open("log.txt","w")as f:
    f.write("Starting log...\n")
    f.write("Processing data...\n")
    f.write("Finished processing.\n")
with open("log.txt","a")as f:
    f.write("DONE\n")

Short Coding Tasks
Count Lines, Words, Characters
with open("input.txt","r",encoding="utf-8")as f:
    data = f.read()
lines = len(data.splitlines())
words = len(data.split())
chars = len(data)
print(f"lines={lines}")
print(f"words={words}")
print(f"chars={chars}")

Filter Lines Containing a Keyword
key = input().strip().lower()
with open("input1.txt","r",encoding="utf-8") as f:
    for line in f:
        if key in line.lower():
            print(line.strip())

Copy File (Text Mode)
with open("input1.txt","r",encoding="utf-8")as src:
    data = src.read()
with open("dest.txt","w",encoding="utf-8")as dst:
    dst.write(data)

Sum Integers from File
total = 0
with open("nums.txt","r",encoding="utf-8")as f:
    for line in f:
        for w in line.split():
            if w.lstrip("-").isdigit():
                total += int(w)
print(total)

Write Results to a New File
with open("input2.txt","r",encoding="utf-8")as f:
    for line in f:
        w = line.lower().strip()
        print(w)

with open("input2.txt","r",encoding="utf-8")as src,\
    open("clean.txt","w",encoding="utf8")as dst:
    for line in src:
        dst.write(line.lower().strip() + "\n")