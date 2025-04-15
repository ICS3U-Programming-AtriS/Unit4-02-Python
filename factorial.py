#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: April 14, 2025
# Program that calculates the product of 1*2*3...*n,
# (AKA a factorial)
# where n is a non-negative integer given by the user.
# The sum will be calculated through the use of a while loop.


def main():
    # Get the user's input as a string
    user_input = input("Enter a non-negative integer: ")

    try:
        # Convert the user's input to an integer
        user_num = int(user_input)

        # Check if the user's number is positive (or 0)
        if user_num >= 0:
            # Initialize variables for the loop
            product = 1
            counter = 0
            while True:
                # Increment counter by 1
                counter += 1
                # Multiply product by counter
                product *= counter
                # Loop while counter is less than user_num
                if (counter >= user_num):
                    break
            # Display the product
            print(f"{user_num}! = {product}.")
        else:
            # Tell the user that the number can't be negative
            print(f"Number must be a non-negative integer!")
    except ValueError:
        # Tell the user that their input wasn't an integer
        print(f"{user_input} is not an integer.")
    finally:
        # Program completion message
        print("Thanks for Playing!")


if __name__ == "__main__":
    main()
