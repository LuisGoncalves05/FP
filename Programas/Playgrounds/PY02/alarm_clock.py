hour = int(input())
minutes = int(input())
hour += 6
minutes += 51
if minutes > 59:
    minutes = minutes % 60 
    hour += 1
if hour > 23:
    hour = hour % 24 

print(str(hour).zfill(2) + ":" + str(minutes).zfill(2))