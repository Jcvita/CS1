def main():
    # stringify()
    lst = [34, 3, 6, 75, 1, 69, 420, 1337, 3]
    bubble(lst)


def stringify(lst=[1, 2, 3, 4, 5]):
    str = '12345'
    str2 = '123123123123'
    tup = ('1, 2', 3, 4, range(5, 7), 8, 9, 10)
    print(str[3:5])
    print(str2.split('3'))
    print(lst[4])
    print(tup)
    print(stringify(lst))
    strlst = []
    for st in lst:
        strlst += str(st)
    return strlst


def bubble(lst):
    while not sorted(lst):
        for x in range(lst) - 1:
            if lst[x] > lst[x + 1]:
                temp = lst[x]           #
                lst[x] = lst[x + 1]     # swap function
                lst[x + 1] = temp       #
    print(lst)


def sorted(lst):
    sort = True
    for x in range(lst):
        if x != 0:
            if lst[x] > lst[x - 1]:
                sort = False
    return sort


main()
