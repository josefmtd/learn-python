def main():
    count = eval(input("Insert amount of numbers in the series: "))
    summation = 0
    for iterator in range(count, 0, -1):
        iterator = eval(input("Insert the number: "))
        summation += iterator
    print("Sum of the series is", summation)

main()
