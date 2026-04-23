my_list = []

def list_manipulation(command, item=None):
    global my_list
    if command == "add":
        if item is not None:
            my_list.append(item)
    elif command == "remove":
        if my_list:
            my_list.pop()
    return my_list

turn = int(input())

for i in range(turn):
    command = (input(f"Command {i+1}: "))
    
    if command == "add":
        item = input()
        print(list_manipulation(command, item))
    elif command == "remove":
        print(list_manipulation(command))
        