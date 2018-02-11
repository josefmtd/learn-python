def main():
    fib1 = 1
    fib2 = 1

    n = eval(input("Insert the number of n:"))

    for count in range(2,n,1):
        temp = fib1+fib2
        fib1 = fib2
        fib2 = temp
    print("The nth fibonacci is:", temp)

main()
