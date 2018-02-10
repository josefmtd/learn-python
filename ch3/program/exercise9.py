import math

def main():
    a, b, c = eval(input("Insert the length of three sides of a triangle (a, b, c): "))
    s = (a + b + c)/2
    A = math.sqrt(s*(s-a)*(s-b)*(s-c))

    print("The area of triangle is", A)

main()
