number = 5
rows = 2*number - 1

for i in range(1, rows+1):
    if i <= number:
        stars = 2*i - 1
    else:
        stars = 2*(rows - i + 1) - 1
    
    spaces = (2*number - 1 - stars) // 2

    for j in range(spaces):
        print("  ", end="")
    
    for j in range(stars):
        if j == 0 or j == stars - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#         *
#       *   *
#     *       *
#   *           *
# *               *
#   *           *
#     *       *
#       *   *
#         *