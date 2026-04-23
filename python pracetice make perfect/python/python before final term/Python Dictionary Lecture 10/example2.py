dictionary = dict()
for i in range(3):
    line = input()
    token = line.split(' ')
    k = token[0]
    v = token[1]
    if k not in dictionary:
        dictionary[k] = []
    dictionary[k] = []
    dictionary[k].append(v)

print(dictionary)