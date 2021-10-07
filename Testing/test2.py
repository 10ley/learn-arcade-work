# Put your code below:
def print_triangle(rows):
    for row in range(rows):
        for column in range(rows - row - 1):
            print(".", end=" ")
        for column in range (row + 1):
            print(column, end=" ")
        for column in range (row - 1, -1, -1):
            print(column, end=" ")
        print()


# Here are some example calls to test your code. Don't change the code below:
print_triangle(5)
print()
print_triangle(3)
print()
print_triangle(9)
