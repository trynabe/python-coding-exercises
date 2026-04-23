# import numpy as np

# def analyze_sales(filename):
#     sales_values = []
#     l_product_sales = []

#     total = lambda price, qty: price * qty

#     with open(filename, "r") as file:
#         for line in file:
#             line = line.strip()
#             code, name, price, qty = line.replace("-", ",").split(",")

#             price = int(price)
#             qty = int(qty)

#             sales_value = total(price,qty)
#             sales_values.append(sales_value)

#             if name.startswith("L"):
#                 l_product_sales.append(sales_value)

#     mean = np.mean(sales_values)
#     std = np.std(sales_values)

#     return {
#         "Mean": mean,
#         "Standard Deviation": std,
#         "Sales for products starting with L": l_product_sales
#     }
# result = analyze_sales("sales.txt")
# print(result)

# Problem 1) — Read the file and count the total number of words.
# count = 0
# with open("data.txt", "r",encoding="utf-8") as f:
#     for line in f:
#         word = line.strip().split()
#         count += len(word)
# print(f"Total word: {count}")

# Problem 2 )— Find the largest number from the file.
# num = []
# with open("numbers.txt","r",encoding="utf-8") as f:
#     for line in f:
#         num.append(int(line.strip()))
# print(f"Max: {max(num)}")

# Problem 3 — Write the results to a new file.
# with open("datatext.txt","r",encoding="utf-8") as f:
#     lines = f.readlines()
# with open("upper.txt","w",encoding="utf-8") as out:
#     for line in lines:
#         text = line.strip()
#         if text.isupper():
#             out.write(text+ "\n")

# Problem 4 — Read a simple CSV file
# score = []
# with open("score.csv","r") as f:
#     for i,line in enumerate(f):
#         if i == 0:
#             continue
#         name, sc = line.strip().split(",")
#         score.append(int(sc))
# avg = sum(score) / len(score)
# print(f"Average Score: {avg:.2f}")

# Problem 5 — Write Log to the end of the file.
# from datetime import datetime
# time_now = datetime.now().strftime("%Y-%m-%d %H:%M")
# with open("log.txt","a") as f:
#     f.write("Your Father Died On " + time_now + "\n")

# Problem 6 — Read the file and find the score greater than 50.
# number = []
# with open("score2.txt") as f:
#     for line in f:
#         number.append(int(line.strip()))
# with open("pass.txt","w") as out:
#     for n in number:
#         if n > 50:
#             out.write(str(n) + "\n")

# Problem 7 — Count the number of occurrences of each word in the file.
# with open("words.txt","r") as f:
#     data = f.read().split()
# freq = {}
# for w in data:
#     if w not in freq:
#         freq[w] = 0
#     freq[w] += 1
# for k , v in freq.items():
#     print(f"{k}: {v}")


# Problem 8 — Add numbers from multiple files.
# files = ["a.txt","b.txt","c.txt"]
# nums = []
# for filename in files:
#     with open(filename) as f:
#         for line in f:
#             nums.append(int(line.strip()))
# print(f"Sum : {sum(nums)}")

# Problem 9 — Read the student files and group them by grade.
# group = {}
# with open("student.txt") as f:
#     for line in f:
#         name, grade = line.strip().split(",")
#         if grade not in group:
#             group[grade] = []
#         group[grade].append(name)
# for grade,name in group.items():
#     print(f"{grade} : {",".join(name)}")

# Problem 10 — Read a matrix from a file and find the sum of each row.
# raw_lines = []
# matrix = []
# with open("matrix.txt") as f:
#     for line in f:
#         raw_lines.append(line.strip())
#         row = list(map(int, line.split()))
#         matrix.append(row)

# for line in raw_lines:
#     print(line)

# with open("matrix.txt") as f:
#     row_output = []
#     for i , line in enumerate(f,start=1):
#         row = list(map(int, line.split()))
#         row_output.append(f"Row {i} sum = {sum(row)}")
#         print(f"Row {i} sum = {sum(row)}")

# cols_output = []
# for c in range(len(matrix[0])):
#     col_sum = 0
#     for r in range(len(matrix)):
#         col_sum += matrix[r][c]
#     cols_output.append(f"Col {c+1} sum = {col_sum}")
#     print(f"Col {c+1} sum = {col_sum}")

# with open("all_result.txt","w") as out:
#     for line in raw_lines:
#         out.write(line + "\n")
#     out.write("\n")
#     for line in row_output:
#         out.write(line + "\n")
#     out.write("\n")
#     for line in cols_output:
#         out.write(line + "\n")

