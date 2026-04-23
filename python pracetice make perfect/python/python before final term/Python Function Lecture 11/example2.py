number = int(input("Enter Your Number : "))
def get_circle_area(r):
    if r > 0:
        r_square = r*r
        return 3.14 * r_square
area1 = get_circle_area(5)
area2 = get_circle_area(0)

print(type(area1))
print(type(area2))