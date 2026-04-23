day = input("วัน : ")
is_member = input("สถานะสมาชิก Yes/No : ")

if day == "Saturday" or day == "Sunday":
    if is_member == "Yes":
        print("You get a 15% discount.")
    elif is_member == "No":
        print("Sorry, no discount today.")

if day == "Wednesday":
    if is_member == "Yes" or is_member == "No":
        print("You get a 10% discount.")

if day == "Monday" or day == "Tuesday" or day == "Thurday" or day == "Friday":
    if is_member == "Yes" or is_member == "No":
        print("Sorry, no discount today.")