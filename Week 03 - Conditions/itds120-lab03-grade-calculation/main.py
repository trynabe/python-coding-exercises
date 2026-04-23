'''
/**
USERID: 6887056
PASSWORD:   
EXERCISEID: itds120-lab03-grade-calculation
 */
'''

# YOUR CODE HERE
Lab = float(input())
Ass = float(input())
Quiz = float(input())
CPE = float(input())
Project = float(input())

#all = 0
all = ((Lab *10/12) + (Ass *10/12) + (Quiz *10/12) + (CPE *50/80) + (Project *20/100))

if  all >= 85:
    print("Grade: A")
elif all >= 80:
    print("Grade: B+")
elif all >= 75:
    print("Grade: B")
elif all >= 70:
    print("Grade: C+")
elif all >= 65:
    print("Grade: C")
elif all >= 60:
    print("Grade: D+")
elif all >= 50:
    print("Grade: D")
else:
    print("Grade: F")