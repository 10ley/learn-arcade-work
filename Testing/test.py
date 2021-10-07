# months = "JanFebMarAprMayJunJulAugSepOctNovDec"
# n = int(input("Enter a month number: "))
# month = months[(n - 1) * 3:(n - 1) * 3 + 3]
# print(month)
my_list = [4, 5, 56, 2, 0]

biggest_number = my_list[0]
for item in my_list:
    if item in my_list:
        if item > biggest_number:
            biggest_number = item

print(biggest_number)