names = [
    {"first":"Darcy", "last":"Rap"},
    {"first":"Kitty", "last":"Wang"},
    {"first":"Mark", "last":"Ton"}
    ]
first_name = list(map(lambda x: x['first'], names))
print(first_name)