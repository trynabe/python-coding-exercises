number = int(input("Enter Your Number : "))
def get_circle_area(r):
    r_square = r*r
    area = 3.14 * r_square
    return area
print(get_circle_area(number))