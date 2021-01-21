#!/usr/bin/env python3
"""function def cat_matrices2D(mat1, mat2, axis=0) concatenates two matrices"""


def cat_matrices2D(mat1, mat2, axis=0):
    """INPUT: two matrices
       OUTPUT: new matrix concatenating the two given matrices
    """
    m1 = [row.copy() for row in mat1]
    m2 = [row.copy() for row in mat2]
    if (axis == 0 and len(m1[0]) != len(m2[0])
            or axis == 1 and len(m1) != len(m2)):
        return None
    if axis == 0:
        m1.extend(m2)
    else:
        for i in range(len(m1)):
            m1[i].extend(m2[i])
    return m1
