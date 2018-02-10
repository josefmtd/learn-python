# Write a program that determines the distance
# to a lightning strike based on the time elapsed
# between the flash and the sound of thunder. The
# speed of sound is approx. 1100 ft/sec 1 mile is 5280 ft

import math

def main():
    time_elapsed = eval(input("Insert the time elapsed between lightning and thunder: "))

    feet_distance = 1100 * time_elapsed
    miles_distance = feet_distance/5280

    print("The distance is", miles_distance, "miles or", feet_distance, "feet")

main()
