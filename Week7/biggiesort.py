"""
Joseph Vita
CSCI-141 Herring
10/9/19

biggiesort.py reads numbers from a file, puts them in a list and sorts
them using the BiggieSort algorithm
"""


def main():
    # file = open(input("Sort which file? "))
    file = open('C:\\Users\\jcvit\\Documents\\CS1\\Week7\\nums')
    lines = file.readlines()
    tempstr = ''
    for line in lines:
        tempstr += line
    lst = tempstr.split('\n')[:-1]

    for x in range(len(lst)):
        lst[x] = int(lst[x])
        
    print("unsorted:")
    print(lst)
    print("sorted")
    print(biggie_sort(lst))


def biggie_sort(lst):
    """
    sorts a list by iterating through the list and swapping the greatest
    integer with the next last place for each element in the list

    precondition: lst must be all integers

    :param lst:
    :return:
    """
    for x in range(len(lst) - 1, 1, -1):
        lst = swap(lst, x, find_max_from(lst, 0, x))
    return lst


def swap(lst, first, second):
    """
    takes in a list and swaps the position of the two inputted indexes

    precondition:first and second
    :param lst:
    :param first:
    :param second:
    :return:
    """
    temp = lst[first]
    lst[first] = lst[second]
    lst[second] = temp
    return lst


def find_max_from(lst, lo, hi):
    """
    takes in a list and returns the nth maximum integer value inside the list

    precondition:lst contains all strings, ints or floats

    """
    max = int(lst[0])

    for x in range(len(lst)):
        if int(lst[lo]) < int(lst[x]) < int(lst[hi]):
            max = int(lst[x])

    return max


if __name__ == '__main__':
    main()
