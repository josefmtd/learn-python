import math

def main():
    x = eval(input("Insert the number: "))
    n = eval(input("Insert the number of iteration: "))
    guess = x/2
    for count in range(n):
        guess = (guess + x/guess)/2

    delta = guess-math.sqrt(x)

    print("The guess is", guess,"and the difference is", delta)

main()
