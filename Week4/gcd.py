"""
Joseph Vita

Program uses two different types of recursion to find the
greatest common divisor of a number
"""


def main():
    """
    Main function runs everything that should be ran
    :return:
    """
    test_gcd_rec()


# def gcd_rec(a, b):
#     """
#     function prints
#     :param a:
#     :param b:
#     :return:
#     """
#     if b <= 1 or a <= 1:
#         print(1)
#         return 0
#     if b >= a:
#         if b % a == 0:
#             print(a)
#             return 0
#         return gcd_rec(b, a - 1)
#     if a > b:
#         if a % b == 0:
#             print(b)
#             return 0

#     return gcd_rec(a, b - 1)


def gcd_rec(a, b):
    """
    function prints
    :param a:
    :param b:
    :return:
    """
    if a <= 0 or b <= 0:
        print("N/A")
        return 0
    elif a == 1 or b == 1:
        print("1")
        return 1
    if a >= b:
        return gcd_rec(a, a % b)


def gcd_iter(a, b):
    """
    determines the greatest common factor of 2 numbers using
    while loop iteration

    :param a:
    :param b:
    :return:
    """
    if b == 0 or a == 0:
        print('N/A')
        return 0
    if a > b:
        count = b
    else:
        count = a
    while count > 0:
        if b % count == 0 and a % count == 0:
            print(count)
            return 0
        count -= 1


def test_gcd_rec():
    """
    Tests gcd_rec by testing it against various different cases
    """
    gcd_rec(1, 1)
    gcd_rec(8, 16)
    gcd_rec(16, 8)
    gcd_rec(5, 7)
    gcd_rec(0, 17)
    gcd_rec(60, 144)


def test_gcd_iter():
    gcd_iter(1, 1)
    gcd_iter(8, 16)
    gcd_iter(16, 8)
    gcd_iter(5, 7)
    gcd_iter(0, 17)
    gcd_iter(60, 144)


if __name__ == '__main__':
    # test_gcd_rec()
    test_gcd_iter()
    # main()

