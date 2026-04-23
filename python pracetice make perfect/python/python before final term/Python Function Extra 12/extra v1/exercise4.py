num = int(input())
word_list = []

for i in range(num):
    word = input()
    word_list.append(word)

def join_word(*args):
    return " ".join(args)

print(join_word(*word_list))

# def join_word(*args):
#     return " ".join(args)

# word = input()
# print(join_word(*word.split()))