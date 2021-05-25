#!/usr/bin/env python3
"""Sensitivity"""

import numpy as np


def sensitivity(confusion):
    """Sensitivity"""

    return confusion.diagonal() / np.sum(confusion, axis=1).T
