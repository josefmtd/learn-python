def main():
    x1, y1 = eval(input("Insert the first coordinate (x1, y1): "))
    x2, y2 = eval(input("Insert the second coordinate (x2, y2): "))

    slope = (y2 - y1)/(x2 - x1)

    print("The slope is", slope)

main()
