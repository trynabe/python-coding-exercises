'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab06-print-coordinate-matrix
 */
'''


n = int(input())
x = int(input())
y = int(input())
a = f"({x},{y})"

for i in range(n):
    for j in range(n):
        b = f"({i},{j})"
        print(b , end=" ")
        if b == a:
            c = False
            break
    if b == a:
        c = False
        break
    print()