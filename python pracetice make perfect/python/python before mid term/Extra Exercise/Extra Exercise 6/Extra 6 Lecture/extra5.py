word = input()

for i in word:
    if i in "aeiou":
        continue
    print(i)