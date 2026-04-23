number = 5

for i in range(1,number+1):
    for j in range(i):
        print("*",end=" ")
    for j in range(i-1,number-1):
        print(" ",end=" ")
    for j in range(i,number):
        print(" ",end=" ")
    for j in range(i,0,-1):
        print("*",end=" ")
    print()
for i in range(1,number+1):
    for j in range(i-1,number):
        print("*",end=" ")
    for j in range(1,i):
        print(" ",end=" ")
    for j in range(i-1):
        print(" ",end=" ")
    for j in range(number-i+1):
        print("*",end=" ")
    print()

# N = 5 

# for i in range(1, N+1):
#     print("* " * i, end='')
#     print("  " * (2*(N-i)), end='')
#     print("* " * i)

# for i in range(N, 0, -1):
#     print("* " * i, end='')
#     print("  " * (2*(N-i)), end='')
#     print("* " * i)
