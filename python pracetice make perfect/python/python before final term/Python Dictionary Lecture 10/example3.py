dictionary1 = {"a": [1,2,3], "b":10}
dictionary2 = dictionary1.copy()

dictionary2['a'].append(4)
dictionary2['b'] = 99

print(dictionary1)
print(dictionary2)
print(dictionary1["a"])
print(dictionary1["b"])

