import math

def main():
    angle = eval(input("Insert the angle: "))
    angle_rad = angle*math.pi/180

    height = eval(input("Insert the height: "))

    length = height/math.sin(angle_rad)
    print("The length is", length)
main()
