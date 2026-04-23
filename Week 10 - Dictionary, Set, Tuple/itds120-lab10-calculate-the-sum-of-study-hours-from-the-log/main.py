'''
/**
USERID: 6887056
PASSWORD: eafd0e

EXERCISEID: itds120-lab10-calculate-the-sum-of-study-hours-from-the-log
*/
'''
number_dict = {}
total = 0

number = int(input("Enter Your Number : "))

for i in range(number):
    z = input("")
    x = float(input(""))
    number_dict[z] = x
    total += x

print(number_dict)
print(total)