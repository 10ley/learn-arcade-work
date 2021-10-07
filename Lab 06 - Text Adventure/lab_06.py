"""
Lab 6 - Rooms
"""


class Room:
    """
    Code for rooms
    """
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    room_list = []
    room = Room("a dark and musky room. East to you is a hallway.", None, 1, None, None)
    room_list.append(room)
    room = Room("dimly lit hallway. West of you is the waiting room."
                " East of you is a common room?", None, 2, 4, 0)
    room_list.append(room)
    room = Room("common area full, the chairs look as if they have been thrown about. "
                " You are next to the north hall", None, None, None, 1)
    room_list.append(room)
    room = Room("an alter room that looks extremely rundown. "
                " You are next to the dimly lit hall.", None, 4, None, None)
    room_list.append(room)
    room = Room("the middle of the dimly lit hallway."
                " East of you is the alter room."
                " To the west is a cell?", 1, 5, 7, 3)
    room_list.append(room)
    room = Room("a jail like room, a monster gleams from within the cage."
                " West of you is the hall", None, None, None, 4)
    room_list.append(room)
    room = Room("office? There is a desk with claw marks."
                "West of you is the hall.", None, 7, None, None)
    room_list.append(room)
    room = Room("south dimly lit hallway."
                " West of you is an office."
                " East of you is a staircase", 4, 8, None, 6)
    room_list.append(room)
    room = Room("dark, and steep staircase."
                " to the south ???...", None, None, 9, 7)
    room_list.append(room)
    room = Room("a room, full of mangled bodies and dismembered limbs."
                " The stairs are to the north.", 8, None, None, None)
    room_list.append(room)

    current_room = 0

    done = False
    while done == False:
        print()
        print("You are in", room_list[current_room].description)
        users_input = input("? ")

        if users_input.lower() == "n" or users_input.lower() == "north":
            next_room = room_list[current_room].north
            if next_room is None:
                print()
                print("You cannot go this way.")
            else:
                current_room = next_room
                print()

        elif users_input.lower() == "e" or users_input.lower() == "east":
            next_room = room_list[current_room].east
            if next_room is None:
                print()
                print("You cannot go this way.")
            else:
                current_room = next_room
                print()

        elif users_input.lower() == "s" or users_input.lower() == "south":
            next_room = room_list[current_room].south
            if next_room is None:
                print()
                print("You cannot go this way.")
            else:
                current_room = next_room
                print()

        elif users_input.lower() == "w" or users_input.lower() == "west":
            next_room = room_list[current_room].west
            if next_room is None:
                print()
                print("You cannot go this way.")
            else:
                current_room = next_room
                print()

        elif users_input.lower() == "q" or users_input.lower() == "quit":
            print("we will be waiting...")
            break

        else:
            print()
            print("I'm sorry, I do not understand")


main()
