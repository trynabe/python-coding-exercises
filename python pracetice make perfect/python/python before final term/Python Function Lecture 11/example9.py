total = 0 #gloabl variable
def increment():
    global total #use global keyword to refer
    total +=1
    return total
print(increment())
print(increment())
print(increment())
    