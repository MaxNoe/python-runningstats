# python-runningstats

[![Build Status](https://travis-ci.org/MaxNoe/python-runningstats.svg?branch=master)](https://travis-ci.org/MaxNoe/python-runningstats)

This is a small module which provides a `Statistics` class
to calculate statistics in an online manner.

The formulas are taken from [Wikipedia](https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Parallel_algorithm).

The module is `numpy` aware, you can fill in more than one value at once:

```{python}
>>> from runningstats import Statistics
>>> import numpy as np
>>> s = Statistics()
>>> s.fill(np.random.normal(size=100))
>>> s.mean
-0.11433712863074698
>>> s.fill(np.random.normal(size=100))
>>> s.mean
-0.022835570703490356
```

Take a look at the [examples notebook](examples/example.ipynb)
