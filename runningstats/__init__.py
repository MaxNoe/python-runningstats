from __future__ import division, absolute_import
import numpy as np


class Statistics():
    '''
    Class for calculating running statistics
    that enables more than one value to be filled in at a time

    algorithms are taken from:
    http://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Parallel_algorithm
    '''
    def __init__(self):
        self._n = 0
        self._mean = 0
        self._M2 = 0
        self._M3 = 0
        self._M4 = 0

    def fill(self, values):
        '''
        update the Statistics with the new data in values

        notation follows Wikipedia: https://goo.gl/s7Dj19
        '''
        B = np.array(values, copy=False, ndmin=1)

        n = len(B)
        mean = B.mean()
        M2 = np.sum((B - mean) ** 2)
        M3 = np.sum((B - mean) ** 3)
        M4 = np.sum((B - mean) ** 4)

        self.update_from_moments(n, mean, M2, M3, M4)

    def update_from_moments(self, n, mean, M2, M3, M4):
        n_A = self._n
        mean_A = self._mean
        M2_A = self._M2
        M3_A = self._M3
        M4_A = self._M4

        n_B = n
        mean_B = mean
        M2_B = M2
        M3_B = M3
        M4_B = M4

        n_X = n_A + n_B
        delta = mean_B - mean_A
        delta_per_n = delta / n_X

        self._n = n_X
        self._mean = (n_A * mean_A + n_B * mean_B) / n_X
        self._M2 = M2_A + M2_B + delta * delta_per_n * n_A * n_B

        self._M3 = (
            M3_A + M3_B +
            delta * delta_per_n**2 * n_A * n_B * (n_A - n_B) +
            3 * delta_per_n * (n_A * M2_B - n_B * M2_A)
        )

        self._M4 = (
            M4_A + M4_B +
            delta * delta_per_n**3 * n_A * n_B * (n_A**2 - n_A*n_B + n_B**2) +
            6 * delta_per_n**2 * (n_A**2 * M2_B + n_B**2 * M2_A) +
            4 * delta_per_n * (n_A * M3_B - n_B * M3_A)
        )

    def update(self, other):
        ''' Update the Statistics object with another statistics object '''
        self.update_from_moments(other._n, other._mean, other._M2, other._M3, other._M4)

    @classmethod
    def combine(cls, iterable):
        s = cls()

        for other in iterable:
            s.update(other)

        return s

    def __len__(self):
        return self._n

    @property
    def mean(self):
        return self._mean

    @property
    def var(self):
        if self._n < 2:
            return np.nan
        return self._M2 / (self._n - 1)

    @property
    def std(self):
        return np.sqrt(self.var)

    @property
    def skewness(self):
        return np.sqrt(self._n) * self._M3 / (self._M2 ** 1.5)

    @property
    def kurtosis(self):
        return self._n * self._M4 / (self._M2 ** 2) - 3

    def __repr__(self):
        if self._n >= 1e5:
            entries = '{: .4g}'.format(float(self._n))
        else:
            entries = '{: 5d}'.format(self._n)

        r = self.__class__.__name__ + '(\n'
        r += '  Entries: ' + entries + '\n'
        r += '  Mean:     {:.4g} \n'.format(self.mean)
        r += '  StdDev:   {:.4g}'.format(self.std)
        r += '\n)'

        return r
