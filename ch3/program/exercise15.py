import math

def main():
    n = eval(input("Insert amount of element of series to approximate pi: "))
    summation = 0
    for count in range(0, n, 1):
        if count%2 == 0:
            summation += 4/(2*count+1)
        else:
            summation -= 4/(2*count+1)

    delta = math.pi - summation
    print("The approximation of pi is", summation)
    print("The difference is", delta)

main()
