import math

def main():
    x1, y1 = eval(input("Insert the first coordinate (x1, y1): "))
    x2, y2 = eval(input("Insert the second coordinate (x2, y2): "))

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    print("The distance is", distance);

main()
