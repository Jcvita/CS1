"""
CSCI-141 Computer Science 1 Recitation Exercise
07-Searching and Sorting

This is starter code for the implementation of bubblesort.
You need to complete the stubbed-out sort() function.
Do NOT add functions or modify the function definitions!
"""

def sorted(lst):
    sort = True
    for x in range(len(lst) - 1):
        if lst[x] > lst[x + 1]:
            sort = False
    return sort


def bubble_sort(lst):
    """
    Takes a list of numbers as input and returns the sorted
    version of that list.
    :param: list of unsorted elements
    :return: the sorted list
    """
    while not sorted(lst):
        for x in range(len[lst]):



def main():
    """
    Reads input from a file, one line at a time, converts
    each line into a list of integers
    :return:
    """
    file = open("input.txt")
    for line in file:
        vline = line.strip()
        values = vline.split(",")
        int_values = []
        for val in values:
            int_values += [int(val)]
        print(bubble_sort(int_values))

if __name__ == '__main__':
    main()