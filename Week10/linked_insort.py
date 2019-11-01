"""
file: linked_insort.py
author: your name here
description: homework
"""

import linked_code

#
# def sorted(lnk):
#     lst = []
#     for x in range(linked_code.length_rec(lnk)):
#         lst.append(linked_code.value_at(lnk, x))
#
#     sort = True
#     for x in range(len(lst) - 1):
#         if lst[x] > lst[x + 1]:
#             sort = False
#
#     return sort


def insert(value, lnk):
    """
    Put the value in the proper spot in the linked list to keep it sorted.
    New nodes are created.
    :param value: the value to add to the sequence of values in the list
    :param lnk: the node at the head of the list
    :return: a (partially) new linked list with the value inserted
    :pre: the list headed by lnk is sorted.
    :post: the link returned refers to a list that is sorted.
    """

    if lnk is None:
        raise IndexError("Out of bounds Error")
    elif value <= lnk.value:
        return linked_code.LinkNode(value, lnk)
    else:
        return linked_code.LinkNode(lnk.value, insert(value, lnk.rest))


def insort(lnk):
    """
    Return a copy of a linked list where all the values are sorted,
    with the lowest value at the head.
    :param lnk: the node at the head of the provided list
    :return: the head node of the sorted linked list
    """

    while lnk is not None:
        insert(lnk.value, lnk)
        lnk = lnk.rest

    return lnk


def pretty_print(lnk):
    """
    Print the contents of a linked list in standard Python format.
    [value, value, value] (Note the spaces.)
    :param lnk: the node at the head of the provided list
    :return: None
    """

    lst = []
    for x in range(linked_code.length_rec(lnk)):
        lst.append(linked_code.value_at(lnk, x))

    print(lst)


if __name__ == '__main__':
    pretty_print(insort(linked_code.mk_linked_list_rec([3, 8, 4, 1, 5, 0])))
    # print(sorted(linked_code.mk_linked_list_rec([1, 2, 3, 4, 5])))
