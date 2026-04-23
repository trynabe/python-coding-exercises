persons = [
    {"name": "Bob", "weight": 60, "height": 1.6},
    {"name": "John", "weight": 70, "height": 1.7},
    {"name": "Ann", "weight": 45, "height": 1.5}
]
def filter_bmi(persons, v):
    persons_with_bmi = list(map(lambda p: {"name": p['name'], "bmi": p['weight'] / (p['height'] ** 2)} ,persons))
    filered = filter(lambda x : x['bmi'] > v, persons_with_bmi)
    result = list(map(lambda f: f["name"], filered))
    return result

print(filter_bmi(persons, 23))