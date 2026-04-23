number = int(input())

x_dict = {}
for i in range(number):
    key_x = input()
    value_x = int(input())
    x_dict[key_x] = value_x

y_dict = {}
for i in range(number):
    key_y = input()
    value_y = int(input())
    y_dict[key_y] = value_y

merged = x_dict.copy()
for key, value in y_dict.items():
    if key in merged:
        merged[key] += value
    else:
        merged[key] = value
print(merged)