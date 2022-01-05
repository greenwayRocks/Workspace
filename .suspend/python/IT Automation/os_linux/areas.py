import math

def triangle(base, height):
    return base*height/2

def rectangle(base, height):
    return base*height

def circle(radius):
    return math.pi*(radius**2)

def donut(outside_rad, inside_rad):
    return circle(outside_rad) - circle(inside_rad)
