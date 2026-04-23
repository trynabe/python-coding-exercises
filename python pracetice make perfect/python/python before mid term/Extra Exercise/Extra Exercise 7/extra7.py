num = int(input())
a = []

for i in range(num):
    x = int(input("num @{}: ".format(i+1)))
    a.append(x)

if len(a) >= 2:
    a[0],a[-1] = a[-1],a[0]

print(a)
# range 5 ครั้ง
# num @1: 5
# num @2: 1
# num @3: 9
# num @4: 3
# num @5: 7
# [7, 1, 9, 3, 5]