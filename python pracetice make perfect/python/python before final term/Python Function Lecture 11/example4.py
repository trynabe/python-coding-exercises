list_number = []

for i in range(5):
    number = int(input("Enter Number: "))
    list_number.append(number)

def sum_even_numbers(list_number):
    total = 0
    for num in list_number:
        if num % 2 == 0:
            total += num
    return total

print(sum_even_numbers(list_number))