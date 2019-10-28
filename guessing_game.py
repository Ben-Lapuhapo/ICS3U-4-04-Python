#!/usr/bin/env python3

# Created by: Ben Lapuhapo
# Created on: OCT 2019
# This program is a guessing game

import random
# this function uses a try statement
random_number = (random.randint(1, 100))  # a number between 0 and 9


def guess():
    while True:
        # input
        print("")
        user_input_string = input("Please enter a number from (0-9) : ")

        # process & output
        try:
            user_input_integer = int(user_input_string)
            for loop_counter in range(user_input_integer):
                print("")
            if user_input_integer > 9:
                print("Number Too High. Enter a Number from (0-9) only.")
            elif user_input_integer == random_number:
                print("Correct Number!! ----->", random_number)
                break
            else:
                print("Wrong Number!! Correct Number is: {0}"
                      .format(random_number))
        except ValueError:
            print("Not A number, The Number is: {0}"
                  .format(random_number))

        finally:
            print("")
            if user_input_integer == random_number:
                print("Thanks for playing")
            else:
                print("Try Again")


if __name__ == "__main__":
    guess()
