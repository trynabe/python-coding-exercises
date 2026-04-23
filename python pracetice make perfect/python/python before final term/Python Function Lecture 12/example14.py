nums = [1, 2, 3, 4, 5]
doubles = list(map(lambda x: x * 2, nums))
evens = list(filter(lambda x: x % 2 == 0 , nums))
odds = list(filter(lambda x: x % 2 == 1 , nums))
print(doubles)
print(evens)
print(odds)

nums = [1, 2, 3, 4, 5]
sum_list = (lambda x : sum(x))(nums)
print(sum_list)

word = ["Saran","Livid","Theo"]
count_letters = (lambda x : len(x))(word)
print(count_letters)

number = [1, 2, 3, 4, 5]
is_even = list(filter(lambda x : x % 2 == 0 , number))
print(is_even)

number = [1, 2, 3, 4, 5]
find_max = (lambda x:sum(x)/len(x))(number) if number else 0
print(find_max)

number = [1, 2, 3, 4, 5]
sum_even = sum(filter(lambda x : x % 2 == 0 , number))
print(sum_even)

args = ["i","hate","lambda"]
join_word = (lambda x: " ".join(x))(args)
print(join_word)

number = [1, 2, 3, 4, 5]
square_all = list(map(lambda x: x**2 , number))
print(square_all)

name = ["Ann", "John", "Max", "Lisa", "Bo", "Mark", "Amy"]
long_name = list(filter(lambda x: len(x) > 3, name))
print(long_name)

scores = {
    "Alice": 90,
    "Bob": 78,
    "Charlie": 85,
    "Diana": 95,
    "Eve": 60
}
high_score = {k:v for k,v in scores.items() if v > 80}
print(high_score)