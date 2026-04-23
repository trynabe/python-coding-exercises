a = int(input())
b = int(input())

def number_compare(a,b):
    if a > b:
        return "First is Greater"
    elif a < b:
        return "Second is Greater"
    else:
        return "Equal"
print(number_compare(a, b))