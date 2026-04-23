num1 = int(input())
num2 = int(input())

def divide(num1,num2):
    if num2 == 0:
        return "Cannot divide by Zero"
    else:
        return num1 / num2
print(f"{num1}/{num2} = {divide(num1,num2)}")