num = int(input())
number_list = []

for i in range(num):
    number = int(input())
    number_list.append(number)

def extreme(*number_list):
    total = 0
    for number in number_list:
        total = total + number
        return total

print(f"{min(*number_list), max(*number_list)}")