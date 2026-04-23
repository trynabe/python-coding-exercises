number = list(map(int, input().split()))
total = 0

def increment():
    global total
    total += 1

for n in number:
    increment()

print(total)