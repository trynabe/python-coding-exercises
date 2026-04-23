num = int(input())

number_list = []

for i in range(num):
    number = int(input())
    number_list.append(number)

def sum_all(*args):
    total = 0
    for n in args:
        total += n
    return total

print(f"Result = {sum_all(*number_list)}")