#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Jan 2022
# Max Num

from random import randint


def biggest(arr):
    bigst = 0

    # get biggest/process
    for num in arr:
        print(f"The random number is: {num}")
        if num > bigst:
            bigst = num

    # return biggest
    return bigst


def main():
    # main function for max number

    # create array with 10 random numbers/process
    arr = [randint(1, 100) for rand in range(10)]

    # calling function
    bigst = biggest(arr)

    # output
    print(f"\nBiggest number is {bigst}")

    # done
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
