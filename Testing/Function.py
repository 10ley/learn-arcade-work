"""
Writing Functions
"""


def hello():
    """Prints Hello!"""
    print("Hello!")


def goodbye():
    print("Goodbye!")


def main():
    hello()
    goodbye()


if __name__ == "__main__":
    main()


def print_number(my_number):
    print(my_number)


print_number(5)
print_number(6)
print_number(22)


def add_numbers(a, b):
    print(a + b)


add_numbers(15, 20)


def sum_two_numbers(a, b):
    result = a + b
    return result


my_result = sum_two_numbers(5, 4)
print(my_result)


def volume_cylinder(radius, height):
    pi = 3.141593653
    volume = pi * radius ** 2 * height
    return volume


my_volume = volume_cylinder(2.5, 5)
print(my_volume)

def calculate_average(a, b):
    """ Calculate an average of two numbers """
    result = (a + b) / 2
    return result


# Pretend you have some code here
x = 45
y = 56

# Wait, how do I print the result of this?
average = calculate_average(x, y)

