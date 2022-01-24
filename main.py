#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Jan 2022
# Max Num

from random import randint


def main():
    # main function for max number

    # create array with 10 random numbers/process
    arr = [randint(1, 100) for rand in range(10)]

    # define biggest variable
    biggest = 0
    arr = [randint(1, 100) for rand in range(10)]

    # get biggest/process
    for num in arr:
        print(f"The random number {num + 1} is: {num}")
        if num > biggest:
            biggest = num

    # output
    print(f"\nBiggest number is {biggest}")

    # done
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
