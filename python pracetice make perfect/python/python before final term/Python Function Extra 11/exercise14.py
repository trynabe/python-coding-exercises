n = int(input())
number_list = []

for i in range(n):
    number = int(input())
    number_list.append(number)

def sum_odd_number(number_list):
    total = 0
    for number in number_list:
        if number % 2 == 1:
            total = total + number
    return total

result = sum_odd_number(number_list)
print(f"Result : {result}")