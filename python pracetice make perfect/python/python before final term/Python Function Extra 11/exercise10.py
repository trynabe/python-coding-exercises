collection = list(map(int, input()).split())
search_term = int(input())

def frequency(collection, search_term):
    count = 0
    for item in collection:
        if item == search_term:
            count += 1
    return count

print(frequency(collection, search_term))