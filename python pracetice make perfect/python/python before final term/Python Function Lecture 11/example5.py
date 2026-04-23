def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
        return count
dollar_count = count_dollar_signs("upper$ $ize")
print(dollar_count)