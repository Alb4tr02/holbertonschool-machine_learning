#!/usr/bin/env python3
"""Score"""

sensitivity = __import__('1-sensitivity').sensitivity
precision = __import__('2-precision').precision


def f1_score(confusion):
    """Score"""

    return 2 * precision(confusion) * sensitivity(confusion) /
(precision(confusion) + sensitivity(confusion))
