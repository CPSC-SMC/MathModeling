# -*- coding: utf-8 -*-
"""
Linear difference equations

Created on Sun May 11 20:00:16 2014

@author: Steven
"""

import numpy as np
import matplotlib.pyplot as plt

def linear_delta(x,a):
    return np.dot(x,a)
    
def plot_linear_delta(n,xinit,a):
    # Computes the first n terms of the difference equation beginning at x0
    # with linear coefficient a and constant coefficient b
    order = len(xinit)
    terms = np.append(xinit,np.zeros((n,1)))
        
    for i in range(n):
        x = np.append([1],terms[i:i+order])
        terms[i+order] = linear_delta(x,a)
    
    lbl = r'$a=%s,\,x_{0..k-1}=%s$' % (a,xinit)
    
    plt.plot(terms,label=lbl)
    
    return terms.T

print plot_linear_delta(10,[0, 1],[0, 1, 1])
print plot_linear_delta(10,[0, 1],[1, -1, -1])


plt.legend(loc='upper left')