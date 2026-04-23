# 1.
# text = "Hello World".lower()
# count = 0
# for w in text:
#     if w in "aeiou":
#         count += 1
# print(count)

# 2.
# number_list = [5,10,2,8,3]
# print(f"Max={max(number_list)} Min={min(number_list)}")

# 3.
# number_list = [1,2,3,4,5,6]
# odd_num = list(filter(lambda x:x % 2 == 1, number_list))
# print(odd_num)

# 4.
# text_input = "banana"
# dic = {}

# for w in text_input:
#     dic[w] = dic.get(w,0) + 1
# print(dic)

# 5.
# text = ["I","love","Python"]
# print(*text[::-1])
# print(*reversed(text))

# 6.
# number = 5
# def fact(number):
#     result = 1
#     for i in range(result,number + 1):
#         result *= i
#     return result
# print(fact(number))

# 7.
# number = list(map(int,input().split()))
# box = []
# for i in number:
#     box.append(i ** 3)
# print(box)

# 8.
# text = "level"
# if text == text[::-1]:
#     print("YES")
# else:
#     print("NO")

# 9.
# text = ["apple","i","love","python"]
# compute = sorted(text,key=lambda x: len(x))
# print(compute)

# 10.
# grade = input().split()
# dict_grade = {"A":4,"B":3,"C":2,"D":1,"F":0}
# score = []
# for g in grade:
#     score.append(dict_grade[g])
# average = sum(score) / len(score)
# print(f"{average}")

# 11.
# number = list(map(int,input().split()))
# def what(number):
#     odd = []
#     even = []
#     for n in number:
#         if n % 2 == 0:
#             even.append(n)
#         else:
#             odd.append(n)
#     return even, odd
# even,odd = what(number)
# print(f"even={even} odd={odd}")

# 12.
# number = list(map(int,input().split()))
# plus = map(lambda x:x * 2, number)
# print(list(plus))

# 13.
# r = int(input())
# dict_info = {}
# for i in range(r):
#     s,n = input().split()
#     n = int(n)
#     if s in dict_info:
#         dict_info[s] += n
#     else:
#         dict_info[s] = n
# print(dict_info)

# 14.
# text = input().split()
# count = 0
# for w in text:
#     if len(w) >= 5:
#         count += 1
# print(count)

# 15.
# import numpy as np
# number = np.array(list(map(int, input().split())))
# mean = np.mean(number)
# std = np.std(number)
# print(f"mean{mean},std={std:.2f}")

# 16.
# import numpy as np
# number = list(map(int,input().split()))
# rows, cols = map(int,input().split())
# matrix = np.array(number).reshape(rows,cols)
# print(matrix)

# 17.
# with open("data1.txt","r") as f:
#     lines = f.readlines()
# print(len(lines))

# 18.
# count = 0
# with open("data2.txt","r") as f:
#     for line in f:
#         word = line.split()
#         count += len(word)
# print(count)

# 19.
# with open("data3.txt","r") as f:
#     lines = f.readlines()
#     f.close()
# error_lines = []
# for line in lines:
#     if "error" in line:
#         error_lines.append(line)
# f = open("output_data1.txt","w",encoding="utf-8")
# for line in error_lines:
#     f.write(line)
# f.close()

# 20.
with open("data4.txt","r") as f:
    lines = f.readlines()
    f.close()
status_count = {}
for line in lines:
    code = line.split()[0]
    if code in status_count:
        status_count[code] += 1
    else:
        status_count[code] = 1
print(status_count)
