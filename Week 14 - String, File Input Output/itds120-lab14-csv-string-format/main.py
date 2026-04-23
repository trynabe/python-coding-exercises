'''
/**
USERID: 6887056
PASSWORD: eafd0e
EXERCISEID: itds120-lab14-csv-string-format
*/
'''
# Your Python code goes here
data = input().split(",")

if not data[2].isdecimal():
    print("invalid input")
else:
    print(f"{data[1]}, {data[0]} is a {data[3]} student and is {data[2]} years old.")