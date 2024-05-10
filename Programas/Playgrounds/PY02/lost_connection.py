import math

pi = math.pi
velocidade = 5

def angulo_pessoas(angulo_A ,angulo_B):
    diferenca_angulos = abs (angulo_A - angulo_B)
    if abs (diferenca_angulos) <= 180:
        deg = abs(diferenca_angulos)
    else:
        deg = 360 - abs(diferenca_angulos)
    rad = 2 * pi * deg / 360
    return rad

def time_until_lost_connection(angulo_A, angulo_B ):
    radianos = angulo_pessoas(angulo_A ,angulo_B)
    t_h = (35/2) / (math.sin (radianos / 2) * (velocidade))
    t_min = 60*t_h
    return round(t_min, ndigits = 3)
