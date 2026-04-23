cm = int(input())

def cm_to_m(cm):
    return cm / 100

def convert_units(fn,values):
    return [fn(v) for v in values]

values = [100, 250, 180]
print(convert_units(cm_to_m,values))