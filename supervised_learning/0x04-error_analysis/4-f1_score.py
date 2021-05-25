#!/usr/bin/env python3
"""Score"""

sensitivity = __import__('1-sensitivity').sensitivity
precision = __import__('2-precision').precision


def f1_score(confusion):
    """Score"""
    mul = precision(confusion) * sensitivity(confusion)
    su = precision(confusion) + sensitivity(confusion)
    return 2 * mul / su
