# x = "foobar"
# print(x[0])
# print(x[3])
# print(x[-1])

# for x in "ITDS120":
#     print(x,end=" ")

# x = "ITDS120"
# print(len(x))

# 1)
# s = "hello"
# print(len(s))

# 2)
# s = "Apple"
# result = s.startswith("A")
# print(result)

# 3)
# s = "hello"
# print(s.upper())

# 4)
# s = "abcd"
# print(s[::-1])

# 5)
# s = "banana"
# count = 0
# for i in s:
#     if i in "aeiou":
#         count += 1
# print(count)

# 6)
# s = " hi "
# print(s.strip())

# 7)
# s = "CR7"
# s2 = s.replace(s,"LM10")
# print(s2)

# 8)
# s = 12345
# check = str(s).isdigit()
# print(check)

# 9)
# s = "I Love You"
# counter = len(s.split())
# print(counter)

# 10)
# s = "a1b2b3"
# result = ""
# for i in s:
#     if i.isdigit():
#         result += i
# print(result)

# 11)
# s = "banana"
# res = ""
# seen = set()
# for c in s:
#     if c not in seen:
#         res += c
#         seen.add(c)
# print(res)

# 12)
# s = "abaac"
# dict_s = {}
# for c in s:
#     dict_s[c] = dict_s.get(c,0) + 1
# print(dict_s)

# 13)
# s = "level"
# print(s == s[::-1])

# 14
# lst = ["Apple","Air","Banana"]
# count = 0
# for i in lst:
#     if i.startswith("A"):
#         count += 1
# print(count)

# 15)
# s = "hello_world_python".split("_")
# chang = s[0]
# for w in s[1:]:
#     chang += w.capitalize()
# print(chang)

# 16)
# text,a,b = input().split()
# a = int(a)
# b = int(b)
# result = text[a:b]
# print(result)

# 17)
# text = "HeLLo"
# count = 0
# for c in text:
#     if c.isupper():
#         count += 1
# print(count)

# 18)
# text = "Stupid"
# check = text.replace("Stupid","******")
# print(check)

# 19)
# text = "I Love to code Python".split()
# result = []
# for w in text:
#     if len(w) > 3:
#         result.append(w)
# print(" ".join(result))

# 20
# text = "abcdef"
# pairs = []
# i = 0
# while i < len(text):
#     pairs.append(text[i:i+2])
#     i += 2
# print(" ".join(pairs))

# 21
# text = input().split()
# longest = ""
# for w in text:
#     if len(w) > len(longest):
#         longest = w
# print(longest)

# 22
# text = input().split()
# result = []
# for w in text:
#     result.append(w.capitalize())
# print(" ".join(result))

# 23
# lst = ["a","b","a","c","b"]
# dont = []
# for w in lst:
#     if lst.count(w)>1 and w not in dont:
#         print(w)
#         dont.append(w)

# 24
# text = input().split()
# res = []
# for w in text:
#     if len(w) > 4:
#         res.append(w[::-1])
#     else:
#         res.append(w)

# 25
# s = input().replace(" ","").lower()
# letter = set(s)
# is_pangram = True
# for c in "abcdefghijklmnopqrstuvwxyz":
#     if c not in letter:
#         is_pangram = False
#         break
# print(is_pangram)

# 26)
# lst = ["a","b","a","c","a","b"]
# max_freq = 0
# for w in set(lst):
#     freq = lst.count(w)
#     if freq > max_freq:
#         max_freq = freq
# print(max_freq)

# 27)
# text = "abcabcabc"
# n = len(text)
# found = False
# for i in range(1,n//2+1):
#     if n % i == 0:
#         pattern = text[:i]
#         if pattern * (n // i) == text:
#             found = True
#             break
# print(found)

# 28)
# text = "aaabbc"
# res = ""
# count = 1
# for i in range(1,len(text)+1):
#     if i < len(text) and text[i] == text[i-1]:
#         count += 1
#     else:
#         res += text[i-1] + str(count)
#         count = 1
# print(res)

# 29)
# text = "ab12cd34"
# res = []
# tmp = text[0]
# for i in range(1,len(text)):
#     if text[i].isdigit() == tmp[-1].isdigit():
#         tmp += text[i]
#     else:
#         res.append(tmp)
#         tmp = text[i]
# res.append(tmp)
# print(res)

# 30)
# lst = ["flower","flow","flight"]
# lst.sort()
# a,b = lst[0] , lst[1]
# i = 0
# while i < len(a) and i < len(b) and a[i] == b[i]:
#     i += 1
# print(a[:i])

# Q1
# s = input()
# result = ""
# for c in s:
#     if c.isalpha():
#         result += c
# print(result)

# Q2
# s = input()
# result = ""
# for c in s:
#     if c.isupper():
#         result += c.lower()
#     elif c.islower():
#         result += c.upper()
#     else:
#         result += c
# print(result)

# Q3
# s = input()
# count_upper = 0
# count_lower = 0
# count_digits = 0
# for c in s:
#     if c.isupper():
#         count_upper += 1
#     elif c.islower():
#         count_lower += 1
#     elif c.isdigit():
#         count_digits += 1
# print(f"{count_upper} {count_lower} {count_digits}")

# Q4
# s = input()
# n = int(input())
# result = ""
# for c in s:
#     result += c * n
# print(result)

# Q5
# s = input().split()
# result = []
# for w in s:
#     if w[0].isupper():
#         result.append(w)
# print(*result)

# Q6
# s = input().replace(" ","")
# freq = {}
# for w in s:
#     if w in freq:
#         freq[w] += 1
#     else:
#         freq[w] = 1
# for k in sorted(freq):
#     print(f"{k}:{freq[k]}",end=" ")

# Q7
# s = input()
# result = ""
# for w in s:
#     if w not in result:
#         result += w
# print(result)

# Q8
# s = input().strip().split()
# result = ""
# for w in s:
#     result += w.capitalize() + " "
# print(result)

# Q9
# s = input().split()
# reversed_word = s[::-1]
# result = " ".join(reversed_word)
# print(result)

# Q10
# s = input()
# result = ""
# for w in s:
#     if w.isdigit() or w in "+-*/":
#         result += w
#     elif w.isalpha():
#         continue
# import re
# part = re.findall(r'\d+|[+\-*/]',result)
# print(" ".join(part))

# Q11
# s = input().split()
# result = []
# for w in s:
#     if w not in result:
#         result.append(w)
# print(" ".join(result))

# Q12
# import re
# s = input()
# number = re.findall(r'-?\d+\.?\d*', s)
# print(" ".join(number))

# Q13
# s = input().split()
# result = []
# for w in s:
#     flag = True
#     for i, c in enumerate(w):
#         if i % 2 == 0 and not c.islower():
#             flag = False
#             break
#         elif i % 2 == 1 and not c.isupper():
#             flag = False
#             break
#     if flag:
#         result.append(w)
# print(*result)

# Q14
# s = input()
# result = ""
# for w in s:
#     if s.count(w) == 1:
#         result += w
# print(result)

# Q15
# s = input()
# result = ""
# count = 1
# for i in range(1, len(s)):
#     if s[i] == s[i-1]:
#         count += 1
#     else:
#         result += s[i-1] + str(count)
#         count = 1
# result += s[-1] + str(count)
# print(result)

# Q16
# s = input()
# chars = []
# for c in s:
#     if c.isalpha():
#         chars.append(c)
# chars = chars[::-1]
# result = ""
# idx = 0
# for c in s:
#     if c.isalpha():
#         result += chars[idx]
#         idx += 1
#     else:
#         result += c
# print(result)

# Q17
# s = input()
# temp = ""
# pairs = []
# for c in s:
#     if c.isalnum() or c == '=':
#         temp += c
#     else:
#         if '=' in temp:
#             pairs.append(temp)
#         temp = ""
# if '=' in temp:
#     pairs.append(temp)
# pairs.sort(key=lambda x: x.split('=')[0])
# print(*pairs)

# Q18
# def roman_to_int(s):
#     values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':200, 'M':1000}
#     total = 0
#     for i in range(len(s)):
#         if i+1 < len(s) and values[s[i]] < values[s[i+1]]:
#             total -= values[s[i]]
#         else:
#             total += values[s[i]]
#     return total
# s = input().split()
# result = []
# for w in s:
#     letters = ""
#     tail = ""
#     for c in w:
#         if c.isalpha():
#             letters += c
#         else:
#             tail += c
#     if all(c in "IVXLCDM" for c in letters) and letters != "":
#         number = roman_to_int(letters)
#         result.append(str(number) + tail)
#     else:
#         result.append(w)
# print(*result)

# Q19
# s = input()
# longest = ""
# n = len(s)
# for i in range(n):
#     for j in range(i+1,n+1):
#         sub = s[i:j]
#         if s.count(sub) > 1:
#             if len(sub) > len(longest):
#                 longest = sub
# print(longest)

# 20
# s = input()
# tokens = []
# current = ""
# for ch in s:
#     if ch.isalpha() or ch.isdigit():
#         current += ch
#     else:
#         if current:
#             tokens.append(current)
#             current = ""
#         tokens.append(ch)
# if current:
#     tokens.append(current)
# print(*tokens)