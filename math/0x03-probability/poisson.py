#!/usr/bin/env python3
"""Calculate a Poisson distribution"""


e = 2.7182818285


class Poisson():
    """ Class Poisson"""

    def __init__(self, data=None, lambtha=1.):
        """Constructor of Poisson"""
        self.lambtha = float(lambtha)
        if data is None and lambtha <= 0:
            raise ValueError("lambtha must be a positive value")
        else:
            if isinstance(data, list):
                if len(data) > 1:
                    self.data = data
                    self.lambtha = float(sum(self.data) / len(self.data))
                else:
                    raise ValueError("data must contain multiple values")
            else:
                raise TypeError("data must be a list")

    def pmf(self, k):
        """ Probability Mass Function of the distribution"""
        x = int(k)
        if x < 0:
            return 0
        x_fact = 1
        for i in range(1, x + 1):
            x_fact = x_fact * i

        f = e ** -self.lambtha * self.lambtha ** x / x_fact
        return f

    def cdf(self, k):
        """ cumulative distribution function"""
        k = int(k)
        if k < 0:
            return 0

        cumulative = 0
        for i in range(k + 1):
            cumulative += self.pmf(i)
        return cumulative
