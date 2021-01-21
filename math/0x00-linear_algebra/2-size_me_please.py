#!/usr/bin/env python3
"""function def matrix_shape(matrix): returns the shape of a matrix:"""


def matrix_shape(matrix=None):
    """INPUT: a matrix
       OUTPUT: the shape of the given matrix
    """
    shape = []
    aux = matrix
    while matrix is not None and type(aux) == type(matrix):
        shape.append(len(aux))
        aux = aux[0]
    return shape
