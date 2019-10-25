"""
Joseph Vita
CSCI-141 Herring
10/22/2019

birthday.py
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class birthday:
    __slots__ = "month", "day", "year"
    month: str
    day: int
    year: int


def main():
    bd_counts = build_dictionary("birthday20000.txt")
    min_count = int(input("Enter a minimum count: "))
    list_birthdays = birthdays_atleast(bd_counts, min_count)
    print("Birthdays occurred at least " + str(min_count) + " times:")
    print(list_birthdays)
    print()
    list_strings = to_strings(list_birthdays)
    print(list_strings)


def find_number_of_


def build_dictionary(file):
    """
    reads a file and creates a dictionary that maps a birthday class object
    to the number of times it has occurred.
    :param file:
    :return:
    """
    lines = open(file)
    for line in lines:
        line = line.split(' ')
        line[2] = line[2].strip('\n')
        print(line)


def birthdays_atleast(bd_counts, min_count):
    """
    creates a list of birthday instances from bd_counts that occurs at least
    min_count times
    :param bd_counts:
    :param min_count:
    :return:
    """
    pass


def to_strings(list_birthdays):
    """
    takes a list of birthdays and creates a list of strings formatted like
    month/day/year

    :param list_birthdays:
    :return:
    """
    pass


if __name__ == '__main__':
    # main()
    build_dictionary('/home/joe/Documents/CS1/Week9/birthday20000.txt')