#!/usr/bin/env python3
"""
function np_cat(mat1, mat2, axis=0) concatenates matrices along a specific axis
"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    INPUT: matrices
    OUTPUT: new matrix result of concatenate the two given matrices
    """
    return np.concatenate((mat1, mat2), axis=axis)
