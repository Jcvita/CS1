"""
Joseph Vita

Program uses two different methods to find the greatest common divisor
of a number and prompts the user to choose which function to use.
"""


def main():
    """
    Main function prompts the user to choose which gcd function to use
    as well as the numbers to use and prints out the result.
    :return:
    """
    print("Select the GCD function to use:")
    print()
    print("1. Recursive")
    print("2. Iterative")
    print()
    choice = input("Please select a function: ")
    print()
    first = int(input("Please enter the first number: "))
    second = int(input("Please enter the second number: "))
    print()
    if choice == "1":
        print("The greatest common denominator is ", gcd_rec(first, second))
    elif choice == "2":
        print("The greatest common denominator is ", gcd_iter(first, second))


def gcd_rec(a, b):
    """
    function prints
    :param a:
    :param b:
    :return:
    """
    if b == 0:
        return a
    else:
        return gcd_rec(b, a % b)


def gcd_iter(a, b):
    """
    determines the greatest common factor of 2 numbers using
    while loop iteration

    :param a:
    :param b:
    :return:
    """
    if b == 0 or a == 0:
        if a == 0 and b != 0:
            return b
        elif b == 0 and a != 0:
            return a
        else:
            return 0
        return 0
    if a > b:
        count = b
    else:
        count = a
    while count > 0:
        if b % count == 0 and a % count == 0:
            return count
        count -= 1


def test_gcd_rec():
    """
    Tests gcd_rec by testing it against various different cases
    """
    print(gcd_rec(1, 1))
    print(gcd_rec(8, 16))
    print(gcd_rec(16, 8))
    print(gcd_rec(5, 7))
    print(gcd_rec(0, 17))
    print(gcd_rec(17, 0))
    print(gcd_rec(60, 144))


def test_gcd_iter():
    """
        Tests gcd_iter by testing it against various different cases
    """
    print(gcd_iter(1, 1))
    print(gcd_iter(8, 16))
    print(gcd_iter(16, 8))
    print(gcd_iter(5, 7))
    print(gcd_iter(0, 17))
    print(gcd_iter(17, 0))
    print(gcd_iter(60, 144))


if __name__ == '__main__':
    # test_gcd_rec()
    # test_gcd_iter()
    main()

