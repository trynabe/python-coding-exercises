a = int(input())
b = int(input())

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def math(a,b,fn):
    return fn(a,b)

print(math(a,b, add))
print(math(a,b, subtract))