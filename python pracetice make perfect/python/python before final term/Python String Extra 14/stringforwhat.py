What is a String?
✔ B. Strings are sequences of characters and immutable.

Which statement creates an empty string?
✔ A. s = ''
✔ B. s = ""
✔ C. s = str()

Indexing & Slicing Given:
s = "Hello, world!"

1. First character: # expect: 'H'
first = s[0]
print(first)

2. Last character: # expect: '!'
last = s[12]
print(last)

3. Slice "Hello": # expect: 'Hello'
hello = s[:5]
print(hello)

4. Slice "world" (no comma, no space): # expect: 'world'
world = s[7:12]
print(world)

5. Slice "world!" using negative indices: # expect: 'world!'
world_excl = s[7:13]
print(world_excl)

Reverse the string: # expect: '!dlrow ,olleH'
reversed_s = s[::-1]
print(reversed_s)

Core String Methods
Multiple choice (select all that apply)
Which lines correctly transform t = "  Data Science  " to "data science"?

✔ A. t.strip().lower()
✔ B. t.lower().strip()

1. Convert to uppercase: # expect: 'MAH-IDOL'
print("mah-idol".upper())

2. Remove leading/trailing spaces: # expect: 'hello'
print("  hello  ".strip())

3. Replace "cat" with "dog": # expect: 'dogapult'
print("catapult".replace("cat","dog"))

4. Find index of substring "lo" in "Hello": # expect: 3
print("Hello".find("lo"))

Splitting & Joining Given:
line = "Alice,Bob,Charlie"

1. Split by comma to a list: # expect: ['Alice', 'Bob', 'Charlie']
name = line.split(",")
print(name)

2. Join names with a space:
joined = " ".join([ "Alice", "Bob", "Charlie" ])
print(joined)

3. Split "  one   two  three    " by any whitespace: # expect: ['one','two','three']
s = "  one   two  three    "
x = s.split()
print(x)

Short Coding Tasks
1. Normalize Names
s = input()
x = [item.strip().lower() for item in s.split(',')]
print(" ".join(x))

2. Count Vowels and Consonants
s = input().strip().lower()
vowels_set = set("aeiou")

vowels = 0
consonants = 0

for c in s:
    if c.isalpha():
        if c in vowels_set:
            vowels += 1
        else:
            consonants += 1

print(f"vowels={vowels}")
print(f"consonants={consonants}")

Palindrome Check (ignore spaces and case)
s = input().lower()
s_clean = s.replace(" ","")
if s_clean == s_clean[::-1]:
    print("palindrome")
else:
    print("not palindrome")

Extract Numbers and Sum
import re
s = input()
numbers = re.findall(r'\d+', s)
numbers = [int(n) for n in numbers]
print(sum(numbers))

Remove word that contain symbols
s = input()
words = s.split()

clean_words = []
for word in words:
    if word.isalpha():
        clean_words.append(word)
result = " ".join(clean_words)
print(result)

Convert from string money to float
s = input().strip()
convert2THB = {
    "USD": 30.0,
    "JPY": 0.25
}
parts = s.split()
amount_str = parts[0]
currency = parts[1]

amount_str = amount_str.replace(",", "")
amount = float(amount_str)
amount_THB = amount * convert2THB[currency]
print(amount_THB)

Encode/Decode a Message
text = input()
key = int(input())
mode = input().strip()

if mode == "decode":
    key = -key

result = ""

for c in text:
    if c.isupper():
        shifted = (ord(c) - ord('A') + key) % 26 + ord('A')
        result += chr(shifted)
    elif c.islower():
        shifted = (ord(c) - ord('a') + key) % 26 + ord('a')
        result += chr(shifted)
    else:
        result += c

print(result)

