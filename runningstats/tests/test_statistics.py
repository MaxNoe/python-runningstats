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


def test_update_result():
    from .. import Statistics
    from scipy.stats import skew, kurtosis

    s1 = Statistics()
    s2 = Statistics()

    data = np.random.normal(1, 2, size=(200, 10))

    for row1, row2 in zip(data[::2], data[1::2]):
        s1.fill(row1)
        s2.fill(row2)

    s1.update(s2)

    assert np.isclose(s1.mean, np.mean(data))
    assert np.isclose(s1.std, np.std(data, ddof=1))
    assert np.isclose(s1.skewness, skew(data, axis=None))
    assert np.isclose(s1.kurtosis, kurtosis(data, axis=None))


def test_combine_result():
    from .. import Statistics
    from scipy.stats import skew, kurtosis

    stats = [Statistics() for i in range(5)]
    data = np.array([np.random.normal(i, 1, size=(100, 10)) for i in range(5)])

    for s, d in zip(stats, data):
        for row in d:
            s.fill(row)

    s = Statistics.combine(stats)

    assert np.isclose(s.mean, np.mean(data))
    assert np.isclose(s.std, np.std(data, ddof=1))
    assert np.isclose(s.skewness, skew(data, axis=None))
    assert np.isclose(s.kurtosis, kurtosis(data, axis=None))
