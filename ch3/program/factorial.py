# factorial.py
#   Program to compute factorial of a number
#   Illustrates for loop with an acumulator

def main():
    n = eval(input("Please enter a whole number: "))
    fact = 1
    for factor in range(2,n+1,1):
        fact = fact * factor
    print("The factorial of", n, "is", fact)

main()
