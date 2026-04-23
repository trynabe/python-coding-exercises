numbers = list(map(int, input().split()))

def list_average(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return sum(numbers) / len(numbers)

print(list_average(numbers))