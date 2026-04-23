def combine_op(op, *args , **kwargs):
    all_nums = list(args) + list(kwargs.values())
    if not all_nums:
        return 0
    if op == "sum":
        return sum(all_nums)
    elif op == "max":
        return max(all_nums)
    elif op == "min":
        return min(all_nums)
    elif op == "avg":
        return sum(all_nums) / len(all_nums)
    else:
        return "Invalid operation"
    
print(combine_op("sum", 1, 2, 3, x=4, y=5))
print(combine_op("max", 1, 10, 2, x=100, y=5))
print(combine_op("avg", 1, 2, 3, x=4, y=5))