import math

def main():
    year = eval(input("Insert the year: "))

    C = year//100
    epact = (8 + (C//4) - C + ((8*C + 13)//25)+11*(year%19))%30

    print("Epact is", epact)

main()
