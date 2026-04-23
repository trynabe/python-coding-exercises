products = [
    {"name": "A", "price": 100},
    {"name": "B", "price": 200},
    {"name": "C", "price": 300}
]
def filter_products(products, min_v, max_v):
    selected_products = list(filter(lambda x : min_v <= x['price'] <= max_v , products))
    selected_names = list(map(lambda x : x['name'] , selected_products))
    return selected_names
print(filter_products(products, 100, 250))