def count_args(*args):
    count = 0
    for i in args:
        count += 1
    return count

word = input().split()
print(count_args(*word))