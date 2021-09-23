"""
Loops
"""
"""
For Loops
"""

# 'for loops' - when you know how many times to loop
# 'while loop' - loop until a condition

# for i in range(5):
#     print("Please,")
# print("Can go to the mall?")

# # Ask the user how many times to print
# def print_about_gum(repetitions):
#     for i in range(repetitions):
#         print("I will not chew gum in class.")
#
#
# repetitions = int(input("How many times should I repeat? "))
# print_about_gum(10)

"""
# Print 1 to 10 V.1
for i in range(10, -1, -1):
    print(i)
"""

# # Print the numbers 1 to 10. V.2
# for i in range(10):
#     # Add one to i, just before printing
#     print(i + 1)

# # Another way to print the numbers 2 to 10
# for i in range(5):
#     print((i + 1) * 2)

# What does this print? Why? NESTING LOOP
# for i in range(3):
#     print("a")
#     for j in range(3):
#         print("b")
#
# print("Done")

# # Loop from 1:00 to 12:59
# for hour in range(1, 13):
#     for minute in range(60):
#         print(hour, minute)

# Keeping a running total
# total = 0
# for i in range(5):
#     new_number = int(input("Enter a number: " ))
#     total = total + new_number
# print("The total is: ", total)

# # What is the value of sum?
# total = 0
# for i in range(1, 101):
#     total += i
# print(total)

# for hello in range(5):
#     print("Hello,")
# print("there.")

"""
While Loop
"""

for i in range(11):
    print(i)

i = 0
# Sentinel variable
while i <= 10:
    print(i)
    i += 1

# i = 10
# while i >= 0:
#     print(i)
#     i -= 1
