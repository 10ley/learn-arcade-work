"""
Lists
"""

# x = 3 and is of type: <class 'int'>
# x = 3.145 and is of type: <class 'float'>
# x = Hi there and is of type: <class 'str'>
# x = True and is of type: <class 'bool'>

"""
# Tuple
x = (2, 3, 4, 5)
print("x =", x, "and is of type:", type(x))
# List
x = [2, 3, 4, 5]
print("x =", x, "and is of type:", type(x))
"""

"""
Functions use ()
Lists use []
"""

# x = [10, 20]
# print(x[0])
#
# # Index is the position of a number in a list
# # Value is the number
#
# x = [3, 8, 7, 0, 5, 5, 2, 1]
# print(x[1])
#
# x = [3, 8, 7, 0, 5, 5, 2, 1]
# # Takes from the other side
# print(x[-1])
#
# # Replace an element
# x[2] = 22
# print(x)
#
# # Blank lists are valid
# x = [3, 7, 3]
# # Length of list
# size = len(x)
# print(size)

# my_list = ["Knife", "Spoon", "Fork"]
#
# for item in my_list:
#     print(item)
#
# for index, value in enumerate(my_list):
#     print("Item", index, "is", value)

# Create an empty list
# my_list = []
#
# for i in range(5):
#     user_input = input("Enter an integer: ")
#     user_input = int(user_input)
#     my_list.append(user_input)
#     print(my_list)
# print()
# print("Final list:", my_list)

# my_list = [2, 3, 6, 5, 9 , 10, 31]
# print(my_list)
#
# my_list.append(100)
# print(my_list)

# Copy of the array to sum
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

# Initial sum should be zero
list_total = 0

# Loop from 0 up to the number of elements
# in the array:
for index in range(len(my_list)):
    # Add element 0, next 1, then 2, etc.
    list_total += my_list[index]


# Print the result
print(list_total)

# Copy of the array to sum
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

# Initial sum should be zero
list_total = 0

# Loop through array, copying each item in the array into
# the variable named item.
for item in my_list:
    # Add each item
    list_total += item

# Print the result
print(list_total)
