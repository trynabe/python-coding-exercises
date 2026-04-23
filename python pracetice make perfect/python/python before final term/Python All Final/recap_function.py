# age = int(input())
# def calculate_ticket_fee(age):
#     if age <= 5:
#         return 0
#     elif 6 <= age <= 60:
#         return 200
#     elif age < 60:
#         return 100
# A = calculate_ticket_fee(age)
# print(A)

# import math
# number = int(input())
# def power_up(number,power = 2):
#     result = math.pow(number,power)
#     return result
# print(power_up(number))

# numbers = input().split()
# def sum_even_numbers(numbers):
#     result = 0
#     for i in numbers:
#         num = int(i)
#         if num % 2 == 0:
#             result += num
#     return result
# print(sum_even_numbers(numbers))

# a = int(input())
# b = int(input())
# c = int(input())
# def flexible_calc(*args,**kwargs):
#     mode = kwargs.get("mode","sum")
#     if mode == "max":
#         return max(args)
#     else:
#         return sum(args)
# print(flexible_calc(a,b,c, mode="sum"))
# print(flexible_calc(a,b,c, mode="max"))

# product = [
#     {"name":"Labtop","price":40000},
#     {"name":"Mouse","price":500},
#     {"name":"Keyboard","price":1500},
#     {"name":"Monitor","price":8000}
# ]
# expensive_items = filter(lambda x: x["price"] > 1000, product)
# result_names = map(lambda x: x["name"].upper(), expensive_items)
# print(list(result_names))

# def create_profile(name,age,*skill,school = "Mahidol",**details):
#     print(f"Name: {name}, Age: {age}")
#     print(f"School: {school}")
#     print(f"Details: {details}")
#     return "Profile Created!"
# create_profile("Saran", 19, "Coding", "Handsome", GPA=3.8, City="Manchester")

# Lambda
# 1) Convert numbers to squares
# x = 10
# square = lambda x: x * x
# print(square(x))

# 2) Check if the number is even or odd.
# x = 10
# is_even = lambda x: x % 2 == 0
# print(is_even(x))

# 3) Find the sum of two numbers.
# a = 10
# b = 30
# sum_all = lambda a,b: a + b
# print(sum_all(a,b))

# 4) Find length of string
# s = "Saran_Jompachoke"
# length = lambda s: len(s)
# print(length(s))

# 5) Convert string to uppercase
# s = "wonderkid.exe"
# bigger = lambda s: s.upper()
# print(bigger(s))

# 6) Returns the first element of the list.
# number = [10,20,30]
# fruits = ["apple","banana","cherry"]
# first = lambda lst: lst[0]
# print(first(number))
# print(first(fruits))

# 7) Return the last element of the list.
# number = [10,20,30]
# fruits = ["apple","banana","cherry"]
# first = lambda lst: lst[-1]
# print(first(number))
# print(first(fruits))


# 8) Add all the numbers in the list (use sum).
# number = [10,20,30,40,50,60,70,80,90,100]
# all_sum = lambda number: sum(number)
# print(all_sum(number))

# 9) Find the maximum value in the list.
# number = [10,20,30,40,50,60,70,80,90,100]
# maxi = lambda number: max(number)
# print(maxi(number))

# 10) Check if the string contains the word “cat”.
# s = ["cat","dog","bird","fish","lion"]
# has_cat = lambda s: "cat" in s
# print(has_cat(s))

# 11) filter only even numbers from the list
# lst = [1,2,3,4,5,6,7,8,9,10]
# number_even = lambda lst: list(filter(lambda x: x % 2 == 0, lst))
# print(number_even(lst))

# 12) map x2 to every element in the list
# lst = [1,2,3,4,5,6,7,8,9,10]
# plus = lambda lst: list(map(lambda x: x*2, lst))
# print(plus(lst))

# 13) map: Convert all names to uppercase.
# s_list = ["kaka","ronaldo","xavi","cruyff","messi","neymar"]
# bigger = lambda s_list : list(map(lambda s: s.upper(),s_list))
# print(bigger(s_list))

# 14) filter: string length > 3 characters
# s_list = ["are","sad","tiger","banana","handsome"]
# m3re = lambda s_list: list(filter(lambda s: len(s) > 3,s_list))
# print(m3re(s_list))

# 15) reduce: Find the product of a list.
# from functools import reduce
# product = lambda lst : reduce(lambda a,b:a*b,lst)
# numbers = [2, 3, 4, 10]
# result = product(numbers)
# print(result)

# 16) Arrange the list of numbers from greatest to least.
# lst = [1,2,3,4,5,6,7,8,9,10]
# softed_lst = lambda lst : sorted(lst,reverse=True)
# print(softed_lst(lst))

# 17) Sort a list of tuples by the second value.
# lst_tuple = [(1, 4), (2, 1), (3, 2)]
# softed_tuper = lambda lst: sorted(lst, key=lambda x:x[1])
# print(softed_tuper(lst_tuple))

# 18) Count the number of strings that begin with the letter A.
# words = ["Apple", "Banana", "Avocado", "Apricot", "Berry"]
# count_A = lambda lst : len(list(filter(lambda s: s.startswith("A"),lst)))
# print(count_A(words))

# 19) sum only positive numbers
# lst = [-1,-2,3,-4,5,-2,4,3,2,1,-4,5,6,-7]
# only_positive = lambda lst : sum(filter(lambda x : x>0, lst))
# print(only_positive(lst))

# 20) Convert list → string separated by comma.
# lst = [1,2,3,4,5]
# join_member = lambda lst : ",".join(map(str,lst))
# print(join_member(lst))

# 21) filter list of list → average > 10
# lst = [[12, 15], [3, 4, 5], [20, 30]]
# filter_avg = lambda lst: list(filter(lambda sublst: sum(sublst)/len(sublst) > 10, lst))
# print(filter_avg(lst))

# 22) Convert dict → list of “key=value”
# dict_x = {"a":1,"b":2}
# dict_to_list = lambda d: [f"{k}={v}" for k,v in d.items()]
# print(dict_to_list(dict_x))

# 23) Sort student dict by score.
# students = [{"name":"Mai","score":11},{"name":"Ran","score":20},{"name":"Mint","score":18}]
# sort_student = lambda lst : sorted(lst,key=lambda x:x["score"],reverse=True)
# print(sort_student(students))

# 24) Sort student dict by score.
# s = ["kaka","ronaldo","muller","cruyff","vini","zidane"]
# longest = lambda lst: max(lst,key=lambda s:len(s))
# print(longest(s))

# 25) count prime in list
# lst_number = [1,2,3,4,5,6,7,8,9,10]
# is_prime = lambda x:x>1 and all(x%i for i in range(2,int(x**0.5)+1))
# count_prime = lambda lst: len(list(filter(is_prime,lst)))
# print(count_prime(lst_number))

# 26) flatten list 2D → 1D
# lst_number = [[1,2],[3,4]]
# flatten = lambda lst:[x for sub in lst for x in sub]
# print(flatten(lst_number))

# 27) map name → abbreviation
# s = ["ricardo kaka","johan cruyff","marco van basten"]
# initial = lambda name : ".".join([p[0] for p in name.split()])+"."
# initial_all = lambda lst: list(map(initial,lst))
# print(initial_all(s))

# 28) normalize list (0–1)
# number = [10,20,30]
# normalize = lambda lst: [(x-min(lst))/(max(lst)-min(lst)) for x in lst]
# print(normalize(number))

# 29) column average of matrix
# matrix = [[1,2,3],[4,5,6]]
# col_avg = lambda m:[sum(col)/len(col) for col in zip(*m)]
# print(col_avg(matrix))

# 30) zip 2 lists in pairs
# a = [1,2]
# b = ["a","b"]
# pair = lambda a,b : list(zip(a,b))
# print(pair(a,b))

students = {}
n = int(input())
for _ in range(n):
    name = input("Name: ")
    scores = list(map(int, input("Scores: ").split()))
    students[name] = scores
average_score = lambda scores: round(sum(scores)/len(scores), 2)
avg_dict = {name: average_score(scores) for name, scores in students.items()}
print(avg_dict)
# Output = {'Yohan Cruyff': 76.67, 'Lionel Messi': 100.0, 'Neymar Jr': 80.0}