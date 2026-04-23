alphabet_count = {}

while True:
    ch = input("Enter an alphabet or -1 to stop: ")
    if ch == "-1":
        break
    if ch in alphabet_count:
        alphabet_count[ch] += 1
    else:
        alphabet_count = 1

total = sum(alphabet_count.values())
print(f"Total alphabet = {total}")

for key, value in alphabet_count.items():
    print(f"{key}:{value}")