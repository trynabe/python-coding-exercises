number = int(input())

def return_day(number):
    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

    if 1 <= number <= 7:
        return days[number - 1]
print(return_day(number))