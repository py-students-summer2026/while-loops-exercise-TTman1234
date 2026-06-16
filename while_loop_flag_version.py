"""
Sings the class American song, "99 Bottles of Beer on the Wall"
using a while loop controlled by a flag.
"""


def get_starting_number():
    prompt = "How many bottles of beer on the wall?"
    response_str = input(prompt)
    stripped_input = response_str.strip()

    if stripped_input.isdigit():
        number = int(stripped_input)
    else:
        number = -1

    if number >= 1:
        return number
    else:
        while True:
            response_str = input(prompt)
            stripped_input = response_str.strip()

            if stripped_input.isdigit():
                number = int(stripped_input)
            else:
                number = -1

            if number >= 1:
                return number


def sing(starting_number):
    current_number = starting_number
    keep_singing = True

    while keep_singing:
        if current_number == 1:
            bottle_word = "bottle"
        else:
            bottle_word = "bottles"

        next_number = current_number - 1

        if next_number == 1:
            next_bottle_word = "bottle"
        else:
            next_bottle_word = "bottles"

        if current_number == 1:
            action = "Take it down, pass it around,"
        else:
            action = "Take one down, pass it around,"

        if next_number == 0:
            next_part = "no more bottles of beer on the wall!"
        else:
            next_part = f"{next_number} {next_bottle_word} of beer on the wall."

        first_line = f"{current_number} {bottle_word} of beer on the wall, {current_number} {bottle_word} of beer."
        second_line = f"{action} {next_part}"

        print(first_line)
        print(second_line)

        if current_number != 1:
            print()

        current_number = current_number - 1

        if current_number == 0:
            keep_singing = False
