'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab07-list-insert-and-update
 */
'''

# YOUR CODE HERE
list_a = []

for i in range(5):
    a = float(input())
    list_a.append(a)

x = float(input())

for i in range(len(list_a)):
    if list_a[i] > x:
        list_a[i] = 'g'
    elif list_a[i] < x:
        list_a[i] = 's'
    else:
        list_a[i] = 'e'
print(list_a)