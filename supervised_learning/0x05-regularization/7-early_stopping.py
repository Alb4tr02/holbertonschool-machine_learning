#!/usr/bin/env python3
"""Early stopping"""


def early_stopping(cost, opt_cost, threshold, patience, count):
    """Early stopping"""

    count = opt_cost - cost <= threshold ? count + 1 : 0
    return (count == patience ? True, count : False, count)
