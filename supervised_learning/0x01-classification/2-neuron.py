#!/usr/bin/env python3
"""First Neuron"""
import numpy as np


class Neuron():
    """Defines a single neuron performing binary classification"""

    def __init__(self, nx):
        """Constructor.

        Args:
            nx (int): number of inputs (Xi).
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        self.nx = nx
        # Private Weight
        self.__W = np.random.randn(nx).reshape(1, nx)
        # Private Bias
        self.__b = 0
        # Private Output
        self.__A = 0

    @property
    def W(self):
        """ W attribute getter.

        Returns:
            ndarray: Private W.
        """
        return self.__W

    @property
    def b(self):
        """ b attribute getter.

        Returns:
            int: Private b.
        """
        return self.__b

    @property
    def A(self):
        """ A attribute getter.

        Returns:
            int: Private A.
        """
        return self.__A

    def forward_prop(self, X):
        """ Calculates neuron output.

        Args:
            X (ndarray): rows X's, cols examples.

        Returns:
            ndarray: vector with activation results using sigmoid.
        """
        # sum(W.X)
        sum_WxX = np.matmul(self.__W, X)
        # -sum(W.X) - b
        z = sum_WxX + self.__b
        # Sigmoid = 1 / 1 + e^(-sum(W.X) - b)
        sigmoid_z = 1 / (1 + np.exp(-z))
        self.__A = sigmoid_z
        return self.__A
