"""
    Joseph Vita

    Python script computes real roots of a quadratic equation and
    prints the equation, roots and the number of roots.
"""
import math


"""
    Function prints equation formatted as a quadratic, number of 
    roots and the roots
    
    precondition:
    postcondition: 
"""
def quadratic_roots(a, b, c):
    print("Equation: ", a, "x^2", "+", b, "x", "+", c, "=", "0")


quadratic_roots(1, 2, 3)