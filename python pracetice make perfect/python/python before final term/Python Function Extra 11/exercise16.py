number_list = []

n = int(input())
for i in range(n):
    number = int(input())
    number_list.append(number)

add_ten = lambda x: x * 2
result = [add_ten(n) for n in number_list]
print(result)