#!/usr/bin/env python3

# Created by: Rohnin. B
# Created on: Sep 2021
# this program calculates percentage of a level ex: 4+ == 97%


def level_calculator(level_input_string):
    # this function calculates percentage of a level ex: 4+ == 97%

    # process
    if level_input_string == "4+":
        level_string = 97
    elif level_input_string == "4":
        level_string = 90
    elif level_input_string == "3+":
        level_string = 83
    elif level_input_string == "3":
        level_string = 78
    elif level_input_string == "3-":
        level_string = 71
    elif level_input_string == "2+":
        level_string = 68
    elif level_input_string == "2":
        level_string = 65
    elif level_input_string == "2-":
        level_string = 61
    elif level_input_string == "1+":
        level_string = 58
    elif level_input_string == "1":
        level_string = 55
    elif level_input_string == "1-":
        level_string = 51
    elif level_input_string == "R":
        level_string = 25
    else:
        level_string = -1

    return level_string


def main():
    # this function gets level_input_string

    # input
    level_input_string_from_user = input(
        "Enter a level you would like to convetrt to a percent: "
    )

    # call functions
    returned_percentage = level_calculator(level_input_string_from_user)

    # output
    print("That would be a {}%.".format(returned_percentage))

    print("\nDone.")


if __name__ == "__main__":
    main()
