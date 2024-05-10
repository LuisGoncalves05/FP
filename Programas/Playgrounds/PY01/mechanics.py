import math
angle = int(input())*math.pi/180  # convert to radians
cos_angle = math.cos(angle)
sin_angle = math.sin(angle)
dist = 18**2/5*cos_angle*sin_angle
print(round(dist))