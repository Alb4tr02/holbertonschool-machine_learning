#!/usr/bin/env python3
"""function def def add_matrices2D(mat1, mat2): adds two 2D matrices:"""


def add_matrices2D(mat1, mat2):
    """INPUT: two arrays
       OUTPUT: two arrays element-wise added:
    """
    result_matrix = []
    for i in range(len(mat1)):
        result_matrix.append([mat1[i][j] + mat2[i][j] for j in range(len(mat1[i]))])
    return result_matrix
