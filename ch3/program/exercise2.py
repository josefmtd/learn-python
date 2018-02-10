# Write a program that calculates the cost
# per square inch of a circular pizza,
# given its diameter and price as input

import math

def main():
    diameter = eval(input("Enter the diameter of pizza: "))
    price = eval(input("Enter the price of pizza: "))

    area = 4 * math.pi * ((diameter/2) ** 2)

    costpersquareinch = area/price
    print("Cost per square inch is: ", costpersquareinch, "$/sq in")

main()
