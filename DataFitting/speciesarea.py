# -*- coding: utf-8 -*-
"""
Species area curve fitting

Created on Fri Aug 22 12:10:17 2014

@author: sbroad
"""

import numpy as np
import matplotlib.pyplot as plt

# Species area curves
# p. 146 of Species-Area Relations

# the data, p. 144 Lesser Antilles
area = np.array([1, 4.9, 40, 2000, 3400, 4500, 30000, 40000])
spec = np.array([3, 5, 9, 80, 40, 39, 84, 76])

# plot the data
plt.close()
plt.plot(area, spec, '+')
plt.title('The species-area curve for the Lesser Antilles')
plt.xlabel('Square miles')
plt.ylabel('Species of amphibians and reptiles')

# the model function, a power curve
# use log-log data, linear fit
p = np.polyfit(np.log(area), np.log(spec),1)
z = p[0]
c = np.exp(p[1])

# plot the power curve
Area = np.exp(np.linspace(0,10.7,51))
plt.plot(Area, c*Area**z,'--')

# plot the fit values for each data point
plt.plot(area, c*area**z, 'o')
