class MnM:
    """ This is a class that represents an M&M. Don't modify it. """
    def __init__(self, color):
        """ Create an M&M with the specified color. """
        self.color = color
        self.flavor = "Chocolate"

def all_green_candy(candy_list):
    # Write your code below this comment
    position = 0
    for candy in candy_list:
        if candy_list[position].color == "Green":
            position += 1
            return True
    return False
    # Write your code above this comment


# These are some test cases
def test_1():
    candy_list = []
    candy_list.append(MnM("Green"))
    candy_list.append(MnM("Green"))
    candy_list.append(MnM("Green"))
    candy_list.append(MnM("Green"))
    candy_list.append(MnM("Green"))
    result = all_green_candy(candy_list)
    print("Test 1, should be True: ", result)

def test_2():
    candy_list = []
    candy_list.append(MnM("Green"))
    candy_list.append(MnM("Green"))
    candy_list.append(MnM("Brown"))
    candy_list.append(MnM("Green"))
    candy_list.append(MnM("Green"))
    result = all_green_candy(candy_list)
    print("Test 2, should be False: ", result)

test_1()
test_2()