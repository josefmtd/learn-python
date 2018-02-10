import math

def main():
    pound = eval(input("Insert the number of pound: "))

    coffee_cost = pound * 10.5
    shipping_cost = pound * 0.86 + 1.5

    print("The cost of this order is: $", coffee_cost + shipping_cost)

main()
