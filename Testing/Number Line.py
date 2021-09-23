# def count_up(start, end):
#     for cur_num in range(start, end + 1):
#         print(cur_num)
#
#
# count_up(5, 10)
# count_up(-10, 0)

done = False
while not done:
    quit = input("Do you want to quit? ")
    if quit == "y":
        done = True
        print("Bye!")
        break

    if not done:
        attack = input("Does your elf attack the dragon? ")
        if attack == "y":
            print("Bad choice, you died.")
            done = True

import random

for i in range(1):
    my_number = random.randrange (5)
    print(my_number)
    if my_number == 0:
        print("Dragon!")
    else:
        print("No dragon.")