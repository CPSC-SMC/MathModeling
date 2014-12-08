# -*- coding: utf-8 -*-
"""
Monte Carlo Integral 2

Created on Fri Dec  5 08:11:10 2014

@author: sbroad
"""

import numpy as np
import numpy.random as rdm
import matplotlib.pyplot as plt

n = 50000
f = lambda x: np.cos(x)**2
x = rdm.normal(size=n)
y = rdm.uniform(size=n)

print np.sqrt(2*np.pi)*np.sum(y <= f(x))/n
u = np.sort(x)
plt.plot(x, y, '.')
plt.plot(u, f(u))
