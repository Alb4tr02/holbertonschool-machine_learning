#!/usr/bin/env python3
"""Precision"""

import numpy as np


def precision(confusion):
    """Precision"""

    return confusion.diagonal() / np.sum(confusion, axis=0)
