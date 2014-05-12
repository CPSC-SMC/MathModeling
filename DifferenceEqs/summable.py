# -*- coding: utf-8 -*-
"""
Difference equations, delta is a function of n

Created on Wed May 07 21:53:14 2014

@author: Steven
"""

import numpy as np
import matplotlib.pyplot as plt

def delta(n):
    #return n**4
    return 1/(float(n)+1)

def plot_delta(n,x0):
    # Computes the first n terms of the difference equation beginning at x0
    # with linear coefficient a and constant coefficient b
    terms = np.zeros((n+1,1))
    terms[0] = x0
    
    for i in range(n):
        terms[i+1] = terms[i]+delta(i)
    
    lbl = r'$x_n=f(n),\,x_0=%.3f$' % (x0)
    
    plt.plot(terms,label=lbl)
    return terms.T

print plot_delta(10,1)