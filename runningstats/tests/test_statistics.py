import numpy as np


def test_mean_result():
    from .. import Statistics

    data = np.random.normal(size=(100, 10))

    s = Statistics()

    for values in data:
        s.fill(values)

    assert np.isclose(s.mean, np.mean(data))


def test_std_result():
    from .. import Statistics

    data = np.random.normal(size=(100, 10))

    s = Statistics()

    for values in data:
        s.fill(values)

    assert np.isclose(s.std, np.std(data, ddof=1))


def test_skewness_result():
    from .. import Statistics
    from scipy.stats import skew

    data = np.random.normal(size=(100, 10))

    s = Statistics()

    for values in data:
        s.fill(values)

    assert np.isclose(s.skewness, skew(data, axis=None))


def test_kurtosis_result():
    from .. import Statistics
    from scipy.stats import kurtosis

    data = np.random.normal(size=(100, 10))

    s = Statistics()

    for values in data:
        s.fill(values)

    assert np.isclose(s.kurtosis, kurtosis(data, axis=None))
