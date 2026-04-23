seconds = int(input(""))

if seconds < 0:
    print("กรุณาใส่จำนวนวินาทีเป็นบวก (>= 0)")
else:
    hours = seconds // 3600
    seconds_left = seconds % 3600
    minutes = seconds_left // 60
    secs = seconds_left % 60

    print(f"{hours:02d}:{minutes:02d}:{secs:02d}")