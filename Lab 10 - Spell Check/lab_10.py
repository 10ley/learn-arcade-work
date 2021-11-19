"""
Lab 10
"""

import re
#
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

dictionary = open("dictionary.txt")

dictionary_list = []

for line in dictionary:
    line = line.strip()

    dictionary_list.append(line)

dictionary.close()

print("---Linear Search---")

line_number = 0
with open("AliceInWonderLand200.txt") as my_text:
    for line in my_text:
        line_number += 1
        word_list = split_line(line)
        for word in word_list:

            key = word.upper()

            current_list_position = 0

            while current_list_position < len(dictionary_list) and dictionary_list[current_list_position] != key:
                current_list_position += 1
            if current_list_position >= len(dictionary_list):
                print("Line", line_number, "possible misspelled word:", word)

print("---Binary Search---")

line_number = 0
with open("AliceInWonderLand200.txt") as my_text:
    for line in my_text:
        line_number += 1
        word_list = split_line(line)
        for word in word_list:

            key = word.upper()
            lower_bound = 0
            upper_bound = len(dictionary_list) - 1
            found = False

            while lower_bound <= upper_bound and not found:

                middle = (lower_bound + upper_bound) // 2
                if dictionary_list[middle] < key:
                    lower_bound = middle + 1
                elif dictionary_list[middle] > key:
                    upper_bound = middle - 1
                else:
                    found = True

            if not found:
                print("Line", line_number, "possible misspelled word:", word)
