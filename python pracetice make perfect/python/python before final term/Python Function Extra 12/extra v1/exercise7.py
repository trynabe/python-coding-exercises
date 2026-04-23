fruit_dict = {}
number = int(input())

for i in range(number):
    fruit = input()
    price = int(input())
    fruit_dict[fruit] = price

def fruit_sorted(**kwargs):
    for key in sorted(kwargs.keys()):
        print(f"{key} : {kwargs[key]}")

fruit_sorted(**fruit_dict)