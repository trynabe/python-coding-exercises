count = 0
words = []

while True:
    message = input()
    if message == "F":
        break
    words.append(message)

for i in range(len(words)):
    if words[i] == "code" or words[i] == "Code" or words[i] == "CODE":
        count += 1

if count == 0:
    print("Matrix Something")
else:
    print(f"somethings {count} bruh sus")