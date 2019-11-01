"""
Joseph Vita
CSCI-141 Herring
10/22/2019

birthday.py reads the file birthday20000.txt and asks the user for the minimum
number count for birthday occurences to return. prints all birthdays that occur
a minimum of min_times
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class birthday:
    __slots__ = "month", "day", "year"
    month: str
    day: int
    year: int


def main():
    """
    builds birthday dictionary and asks the user to input a min count.
    prints out birthdays that occur a min of min_count times.
    :return:
    """
    bd_counts = build_dictionary("birthday20000.txt")
    min_count = int(input("Enter a minimum count: "))
    list_birthdays = birthdays_atleast(bd_counts, min_count)
    print("Birthdays occurred at least " + str(min_count) + " times:")
    print(list_birthdays)
    print()
    list_strings = to_strings(list_birthdays)
    print(list_strings)


def build_dictionary(file):
    """
    reads a file and creates a dictionary that maps a birthday class object
    to the number of times it has occurred.
    :param file:
    :return:
    """
    dict = {}
    lines = open(file)
    for line in lines:
        line = line.split(' ')
        line[2] = line[2].strip('\n')
        bday = birthday(line[0], int(line[1]), int(line[2]))
        if bday not in dict:
            dict[bday] = 1
        else:
            dict[bday] += 1

    return dict


def times_in(lst, obj):
    """
    returns the number of times obj appears in lst
    :param lst:
    :param obj:
    :return:
    """
    count = 0
    for x in lst:
        if obj == x:
            count += 1
    return count

def birthdays_atleast(bd_counts, min_count):
    """
    creates a list of birthday instances from bd_counts that occurs at least
    min_count times
    :param bd_counts:
    :param min_count:
    :return:
    """
    at_least = []
    for bday in bd_counts:
        if bd_counts[bday] >= min_count:
            at_least.append(bday)

    return at_least

def to_strings(list_birthdays):
    """
    takes a list of birthdays and creates a list of strings formatted like
    month/day/year

    :param list_birthdays:
    :return:
    """
    strlst = []
    for x in range(len(list_birthdays)):
        strlst.append(str(list_birthdays[x].month) + '/' +
                      str(list_birthdays[x].day) + '/' +
                      str(list_birthdays[x].year))
    return strlst

if __name__ == '__main__':
    main()