"""
Lab 4 - Camel (Dragon)
"""

import random


def main():
    print("""Welcome to Dragon Escape!
You have just stolen gold from the dragon!
He is trailing behind you after his treasure!
You and your horse must outrun him.
Outrun him and reach the forest!""")

    done = False

    dragon = -20
    miles_traveled = 0
    carrots_left = 3
    horse_hunger = 0
    tiredness = 0

    while not done:
        print()
        print("""A. Feed horse.
B. Ahead moderate speed.
C. Ahead full speed.
D. Stop and rest.
E. Status check.
Q. Quit.""")
        user_choice = input("What do you do? ")

        # User Quits
        if user_choice.lower() == "q":
            done = True

        # User travels at moderate speed
        elif user_choice.lower() == "b":
            mi_this_turn = random.randrange(5, 13)
            miles_traveled = miles_traveled + mi_this_turn
            tiredness = tiredness + random.randrange(1, 2)
            dragon = dragon + random.randrange(7, 14)
            horse_hunger = horse_hunger + 1
            print("You traveled " + str(mi_this_turn) + " miles.")
            farm = random.randrange(20)

            if farm == 0:
                print("You found a farm.")
                carrots_left = 3
                print("Carrots have been restocked.")

        # Feeding horse
        elif user_choice.lower() == "a":
            if carrots_left > 0:
                carrots_left = carrots_left - 1
                horse_hunger = 0

        # Travel full speed
        elif user_choice.lower() == "c":
            mi_this_turn = random.randrange(10, 21)
            miles_traveled = miles_traveled + mi_this_turn
            tiredness = tiredness + random.randrange(1, 3)
            dragon = dragon + random.randrange(7, 14)
            horse_hunger = horse_hunger + random.randrange(1, 3)
            print("You traveled " + str(mi_this_turn) + " miles.")
            farm = random.randrange(20)

            if farm == 0:
                print("You found a farm.")
                carrots_left = 3
                print("Carrots have been restocked.")

        # Rest for the night
        elif user_choice.lower() == "d":
            tiredness = 0
            dragon = dragon + random.randrange(7, 14)
            horse_hunger = horse_hunger + 1
            print("You have rested for the night!")

        # Status check
        elif user_choice.lower() == "e":
            print("You have traveled " + str(miles_traveled) + " miles.")
            print("The dragon is " + str(miles_traveled - dragon) + " miles behind you.")
            print("You have " + str(carrots_left) + " carrots left.")

        # Horse hunger
        if horse_hunger >= 7:
            print()
            print("Your horse died of hunger!")
            break

        elif horse_hunger >= 5:
            print()
            print("Your horse is hungry.")

        if tiredness >= 8:
            print()
            print("You died of exhaustion")
            break

        # Tiredness
        elif tiredness >= 5:
            print()
            print("You and your horse are tired.")

        if (miles_traveled - dragon) <= 15:
            print()
            print("The dragon is close.")

        elif dragon >= miles_traveled:
            print()
            print("You have been caught by the dragon!")
            done = True

        if miles_traveled >= 200:
            print()
            print("You have escaped the dragon!")
            done = True


if __name__ == '__main__':
    main()
