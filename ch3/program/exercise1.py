# Write a program to calculate the volume and surface
# area of a sphere from its radius as input

import math

def calculateVolume(radius):
    v = 4/3 * math.pi * (radius ** 3)
    return v

def calculateArea(radius):
    a = 4 * math.pi * (radius ** 2)
    return a

def main():
    r = eval(input("Insert number of radius: "))
    print("Volume is", calculateVolume(r))
    print("Area is", calculateArea(r))

main()
