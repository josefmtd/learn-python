import math

def main():
    n = eval(input("Insert n, number of natural numbers added: "))
    summation = 0

    for iterator in range(n, 0, -1):
        summation += (iterator ** 3)
    print("The sum of cubes is", summation)

main()
