def function_C(*args, **kwargs):
    print(f"ของไม่มีชื่อ (args): {args}")
    print(f"ของมีชื่อ (kwargs): {kwargs}")
function_C(1,2, name="A", job="Student")