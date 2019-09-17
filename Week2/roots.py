"""
    Joseph Vita
    9/5/19

    Python script computes real roots of a quadratic equation and
    prints the equation, roots and the number of roots.
"""
import math


def quadratic_roots(a, b, c):
    """
        Function prints equation formatted as a quadratic, number of
        roots and the roots
    """
    print("Equation: ", a, "x^2", " + ", b, "x", " + ", c, " = ", "0", sep="")
    disc = (b ** 2) - (4 * a * c)

    if disc > 0:
        root1 = ((-b + math.sqrt(disc)) / (2 * a))
        root2 = ((-b - math.sqrt(disc)) / (2 * a))
        print("Two Roots.")
        print("x = ", root1)
        print("x = ", root2)
    elif disc == 0:
        root = ((-b + math.sqrt(disc)) / (2 * a))
        print("One Root.")
        print("x = ", root)
    else:
        print("No roots.")


def test_zero():
    quadratic_roots(4, 1, 4)
    quadratic_roots(4, 16, 64)
    quadratic_roots(333, -2, 66)


def test_one():
    quadratic_roots(1, 0, 0)
    quadratic_roots(1, 4, 4)
    quadratic_roots(1, 12, 36)



def test_two():
    quadratic_roots(2, -11, -21)
    quadratic_roots(1, 10, 16)
    quadratic_roots(35, 38, -2)
    quadratic_roots(-3, -14, 147)


test_zero()
test_one()
test_two()

