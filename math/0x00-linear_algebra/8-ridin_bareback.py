#!/usr/bin/env python3
"""function mat_mul(mat1, mat2) performs matrix multiplication"""


def mat_mul(mat1, mat2):
    """INPUT: two matrices
       OUTPUT: new matrix product of two matrices given
    """
    matrix = []
    if len(mat1[0]) != len(mat2):
        return None
    for i in range(len(mat1)):
        matrix.append([sum([mat1[i][k] * mat2[k][j] for k in range(len(mat2))])
                       for j in range(len(mat2[0]))])
    return matrix
