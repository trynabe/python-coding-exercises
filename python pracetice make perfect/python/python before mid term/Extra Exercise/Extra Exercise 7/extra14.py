row = 2
colomn = 3

matrix = []

for i in range(row):
    row_list = []
    print(f"Row {i+1}")
    for j in range(colomn):
        x = int(input("Colomn : "))
        row_list.append(x)
    matrix.append(row_list)

for i in range(colomn):
    for j in range(row):
        print(matrix[j][i],end=" ")
    print()
