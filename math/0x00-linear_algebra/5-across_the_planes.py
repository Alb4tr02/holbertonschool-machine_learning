#!/usr/bin/env python3
"""function def def add_matrices2D(mat1, mat2): adds two 2D matrices:"""


def add_matrices2D(mat1, mat2):
    """INPUT: two arrays
       OUTPUT: two arrays element-wise added:
    """
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    result_matrix = []
    for i in range(len(mat1)):
        row = [mat1[i][j] + mat2[i][j] for j in range(len(mat1[i]))]
        result_matrix.append(row)
    return result_matrix
