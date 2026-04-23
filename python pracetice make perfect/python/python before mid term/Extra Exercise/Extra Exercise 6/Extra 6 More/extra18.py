N = 5

for i in range(1, N+1):
    print("*", end='')
    if i > 1:
        print(" " * (2*i - 3), end='')
        print("*", end='')
    print(" " * (2*(N-i)*2), end='')
    print("*", end='')
    if i > 1:
        print(" " * (2*i - 3), end='')
        print("*", end='')
    print()
    
for i in range(N, 0, -1):
    print("*", end='')
    if i > 1:
        print(" " * (2*i - 3), end='')
        print("*", end='')
    print(" " * (2*(N-i)*2), end='')
    print("*", end='')
    if i > 1:
        print(" " * (2*i - 3), end='')
        print("*", end='')
    print()


# *                *
# * *            * *
# *   *        *   *
# *     *    *     *
# *       **       *
# *       **       *
# *     *    *     *
# *   *        *   *
# * *            * *
# *                *
