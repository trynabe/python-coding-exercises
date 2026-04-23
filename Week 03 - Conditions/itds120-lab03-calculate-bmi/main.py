'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab03-calculate-bmi
 */
'''

# YOUR CODE HERE
w = float(input())
h = float(input())

bmi = w / (h/100*h/100)

if bmi <= 18.5:
    print("Underweight")
elif bmi <= 24.9:
    print("Normal")
elif bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")