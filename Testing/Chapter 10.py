"""
"If" Statements
"""
# # "Conditional Logic"
#
# a = 4
# b = 5
# c = 6
# # And
# if a < b and a < c:
#     print("a is less than b and c")
#
# # Non-exclusive or
# if a < b or a < c:
#     print("a is less than either b or c (or both)")

# a = 3
# b = 3
#
# # This next line is strange-looking, but legal.
# # c will be true or false, depending if
# # a and b are equal.
# c = a == b
#
# # Prints value of c, in this case True
# print(c)

# if 1:
#     print("1")
# if "A":
#     print("A")
"""
The code below will not print out
anything because the value in the if statement is zero. 
The value zero is treated as False.
Any value other than zero 
(like 2, -1, 600, or even “Fred”) is considered True.
"""
# if 0:
#     print("0")

temperature = int(input("What is the temperature in Fahrenheit? "))
# temperature = int(temperature)
if temperature >= 90:
    print("It is hot outside.")
elif temperature >= 110:
    print("Oh man, you could fry eggs on the pavement!")
elif temperature <= 30:
    print("It is cold outside.")
else:
    print("It is ok outside.")
print(f"You said the temperature was {temperature}.")
print("Done")
