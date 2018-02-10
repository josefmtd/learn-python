# Write a program that determines the molecular
# weight of a hydrocarbon based on the number of
# hydrogen, carbon, and oxygen atoms.

def main():
    carbon_mole = eval(input("Insert the number of carbon moles: "))
    hydrogen_mole = eval(input("Insert the number of hydrogen moles: "))
    oxygen_mole = eval(input("Insert the number of oxygen moles: "))

    hydrocarbon_weight = carbon_mole * 12.011 + hydrogen_mole * 1.0079 + oxygen_mole * 15.9994

    print("The weight of the hydrocarbon is:", hydrocarbon_weight)

main()
