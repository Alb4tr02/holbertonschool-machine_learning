#!/usr/bin/env python3
"""function def matrix_transpose(matrix): returns the transpose of a matrix:"""


def matrix_transpose(matrix):
    """INPUT: a matrix
       OUTPUT: the transpose of the given matrix
    """
    rows, columns = len(matrix), len(matrix[0])
    matrix_t = []
    for i in range(columns):
        matrix_t.append([row[i] for row in matrix])
    return matrix_t
