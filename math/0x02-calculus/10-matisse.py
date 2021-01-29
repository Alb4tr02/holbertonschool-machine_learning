#!/usr/bin/env python3
""" Derivation """


def poly_derivative(poly):
    """
    INPUT: polynomial
    OUTPUT derivative of the polynomial
    """
    if len(poly) == 0 or type(poly) is not list:
        return None

    if type(poly[0]) is not int and type(poly[0]) is not float:
        return None

    derivative = [poly[i] * i for i in range(len(poly))]
    derivative = derivative[1:] if len(derivative) > 1 else derivative
    derivative = [0] if not any(derivative) else derivative
    return derivative
