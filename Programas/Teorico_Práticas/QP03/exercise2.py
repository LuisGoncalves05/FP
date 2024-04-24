hours = int(input())
minutes = int(input())
am_pm = ""

if hours == 0:
    hours = 12
    am_pm = "am"
elif 0 < hours < 12:
    am_pm = "am"
elif hours == 12:
    am_pm = "pm"
elif 12 < hours < 24:
    hours -= 12
    am_pm = "pm"
else:
    print("INVALID DATE FORMAT")

if 0 <= hours < 24:
    if minutes == 0:
        print (f"{hours} {am_pm}")
    elif 0 < minutes < 60:
        print (f"{hours}:{minutes:02d} {am_pm}")
    else:
        print("INVALID DATE FORMAT")
