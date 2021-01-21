#!/usr/bin/env python3
"""function def def add_arrays(arr1, arr2): adds two arrays element-wise::"""


def add_arrays(arr1, arr2):
    """INPUT: two arrays
       OUTPUT: two arrays element-wise added:
    """
    if len(arr1) != len(arr2):
        return None
    return [arr1[i] + arr2[i] for i in range(len(arr1))]
