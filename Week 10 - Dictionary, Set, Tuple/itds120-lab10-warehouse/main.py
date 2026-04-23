'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab10-warehouse
*/
'''
number = int(input(""))
warehouse = {}

for i in range(number):
    x = int(input(""))
    y = int(input(""))
    product = input("")

    if (x,y) not in warehouse:
        warehouse[(x,y)] = set()

    warehouse[(x,y)].add(product)

count_dict = {coord: len(items) for coord, items in warehouse.items()}
print(count_dict)