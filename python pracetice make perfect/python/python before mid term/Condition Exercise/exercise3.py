age = int(input("อายุ : "))
day = input("วัน : ")

if 0 <= age <= 12:
    if day == "Weekday":
        print("Ticket Price: 150 Baht")
    elif day == "Weekend":
        print("Ticket Price: 200 Baht")
if 13 <= age <= 59:
    if day == "Weekday":
        print("Ticket Price: 300 Baht")
    elif day == "Weekend":
        print("Ticket Price: 400 Baht")
if 60 <= age:
    if day == "Weekday":
        print("Ticket Price: Free")
    elif day == "Weekend":
        print("Ticket Price: Free")
