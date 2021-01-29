#!/usr/bin/env python3
"""Sigma square"""


def summation_i_squared(n):
    """
    INPUT a number
    OUTPUT summation of first n numbers squared
    """
    if type(n) is not int or n < 0:
        return None
    return 0 if n == 0 else int(n * (n + 1) * (2 * n + 1) / 6)
