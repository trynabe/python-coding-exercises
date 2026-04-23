matrix = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(3):
    row_sum = 0
    for j in matrix[i]:
        row_sum += j
    print(f"Row {i+1} Sum = {row_sum}")
# OUTPUT
# Row 1 Sum = 6
# Row 2 Sum = 15
# Row 3 Sum = 24
