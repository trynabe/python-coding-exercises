# 1) Count Dictionary Keys
# dict = {"name":"John", "age":30, "city":"Manchester"}
# count = 0
# for key in dict:
#     count += 1
# print(count)

# 2) Add New Key-Value to Dictionary
# dict = {"name":"Ricardo","age":41,"city":"Brazil"}
# dict["football_club"] = "Real Madrid"
# print(dict)

# 3) Update Value in Dictionary
# dict = {'name': 'Ricardo', 'age': 41, 'city': 'Brazil', 'football_club': 'Real Madrid'}
# dict['football_club'] = "AC Milan"
# print(dict)

# 4) Remove a Key from Dictionary
# dict = {'name': 'Ricardo', 'age': 41, 'city': 'Brazil', 'football_club': 'AC Milan'}
# dict.pop("football_club")
# print(dict)

# 5) Check if Value Exists in Dictionary
# dict = {'name': 'Ricardo', 'age': 41, 'city': 'Brazil', 'football_club': 'AC Milan'}
# key = input()
# if key in dict:
#     print("Key found")
# else:
#     print("Key not found")

# 6) Merge Two Dictionaries
# dict_kaka = {'name': 'Ricardo', 'age': 41, 'city': 'Brazil', 'football_club': 'AC Milan'}
# dict_ronaldo = {'name': 'Ronaldo', 'age': 45, 'city': 'Brazil', 'fooball_club': 'Retire'}
# result = dict_kaka | dict_ronaldo
# print(result)

# 7) Create Dictionary from List of Pairs
# data = [["A", 10], ["B", 20], ["C", 30]]
# my_dict = {}
# for pair in data:
#     key = pair[0]
#     value = pair[1]
#     my_dict[key] = value
# print(my_dict)

# 8) Find the Person with Highest Score
# dict_career = {"ronaldo":{"trophy":45},"neymar":{"trophy":34}}
# print(max(dict_career))

9) Extract Names from Nested Dictionary
dict_career1 = {"name":"ronaldo","trophy":45,"ballor":2}
dict_career2 = {"name":"messi","trophy":46,"ballor":7}
dict_career3 = {"name":"cruyff","trophy":33,"ballor":3}
career = {
    "player1":dict_career1,
    "player2":dict_career2,
    "player3":dict_career3
}
for player in career:
    print(career[player]["name"])

# 10) Analyze Sales Data in Dictionary
# product = {
#     "product1": {"name": "adidas predator", "price": 9800},
#     "product2": {"name": "nike phantom", "price": 8990},
#     "product3": {"name": "adidas F50", "price": 9500},
#     "product4": {"name": "nike tiempo", "price": 8550}
#     }
# cost = 0
# for i in product:
#     cost += product[i]["price"]
# print(f"Total : {cost}")

# max_price = 0
# expensive_product = ""
# for i in product:
#     price = product[i]["price"]
#     if price > max_price:
#         max_price = price
#         expensive_product = product[i]["name"]
# print(f"Most Expensive : {expensive_product}")
# print(f"Price : {max_price}")