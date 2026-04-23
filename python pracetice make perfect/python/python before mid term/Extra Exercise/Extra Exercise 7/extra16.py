number = 3
matrix = []

for i in range(number):
    row_list = []
    for j in range(number):
        x = int(input())
        row_list.append(x)
    matrix.append(row_list)

main_sum = 0
secondary_sum = 0

for i in range(number):
    main_sum += matrix[i][i]
    secondary_sum += matrix[i][number-1-i]

print(f"Main diagonal sum = {main_sum}")
print(f"Secondary diagonal sum = {secondary_sum}")