def add(x, y):
    return x+y

def sub(x, y):
    return x-y

def mul(x,y):
    return x * y

def div(x,y):
    return x / y

def apply_pairwise(fn, a, b):
    return [fn(x, y) for x, y in zip(a, b)]

x = [1, 2, 3]
y = [4, 5, 6]

print(f"Q5 add: {apply_pairwise(add, x, y)}")
print(f"Q5 mul: {apply_pairwise(mul, x, y)}")