#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: October 2019
# This program finds the average of 10 random numbers from 0-100


import random


def main():
    # this function shows the average of 10 random numbers

    list = []

    # generate numbers
    counter = 0
    for counter in range(0, 10):
        random_number = random.randint(0, 100)
        list.append(random_number)
        counter += 1

    # show random numbers
    counter = 0
    for counter in range(0, 10):
        print(list[0+counter])
        counter += 1

    # calculate average
    counter = 1
    list_avg = list[0]
    for counter in range(0, 9):
        list_avg = list_avg + list[0+counter]
        counter += 1

    list_avg = list_avg / 10

    # show average
    print(list_avg)


if __name__ == "__main__":
    main()
