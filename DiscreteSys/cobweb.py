# -*- coding: utf-8 -*-
"""
Cobweb plot

@author: sbroad
"""

import numpy as np
import matplotlib.pyplot as plt


def cobweb(x0, f, ginv = lambda x: x, n = 20):
    """
    Produces a cobweb plot of f vs. g (default g(x)=x))
    
    f ---> the function with a fixed/equilibrium point
    ginv ---> the inverse of the function against which to find equilibrium
         ---> default ginv is identity map
    n ---> the number of cobweb iterations to use (default 20)
    """

    x = x0    
    xmax = x
    xmin = x
    ymax = f(x)
    ymin = f(x)
    for i in range(n):
        xnew = ginv(f(x))
        X = [x, xnew, xnew]
        Y = [f(x), f(x), f(xnew)]
        plt.plot(X, Y, 'k--')
        x = xnew
        xmax = max(xmax, x)
        xmin = min(xmin, max(x,0))
        ymax = max(ymax, f(x))
        ymin = min(ymin, max(f(x),0))
    
    return [xmin, xmax, ymin, ymax]

def supply(p):
    return 2*p+10

def demand_price(x):
    return 100./x

plt.close()
lims = cobweb(12, demand_price, ginv = supply)

x = np.linspace(lims[0] - 1, lims[1] + 1, 21)
y = np.linspace(lims[2] - 1, lims[3] + 1, 21)
plt.plot(supply(y), y, label = 'supply')
plt.plot(x, demand_price(x), label = 'demand')
plt.title('Cobweb plot of supply vs. demand')
plt.xlabel('Quantity produced / purchased')
plt.ylabel('Price')
plt.legend()



        
        