list_number = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
result = []
for i in list_number:
    count = 0
    for x in i:
        if x % 2 == 0:
            count += 1
    result.append(count)
print(result)