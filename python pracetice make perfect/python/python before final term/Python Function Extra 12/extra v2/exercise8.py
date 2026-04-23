input_str = input("")
str_list = input_str.split()

number_list = []
for i in str_list:
    number_list.append(int(i))

def sum_nested(list_to_sum):
    result = sum(list_to_sum)
    total = 0
    total += total + result
    return total

final_sum = sum_nested(number_list)
print(final_sum)