# -*- coding: utf-8 -*-
"""
Created on Wed May  7 17:08:42 2014

@author: sbroad
"""

import numpy as np
import matplotlib.pyplot as plt

def first_order_linear(xn, a, b):
    # Computes the x_(n+1) term of a difference equation given the x_n term
    # xn --> the x_n term
    # a  --> the linear coefficient of the difference equation
    # b  --> the constant coefficient of the difference equation
    return a*xn+b

def plot_fol(n,x0,a,b):
    # Computes the first n terms of the difference equation beginning at x0
    # with linear coefficient a and constant coefficient b
    terms = np.zeros((n+1,1))
    terms[0] = x0
    
    for i in range(n):
        terms[i+1] = first_order_linear(terms[i],a,b)
    
    lbl = r'$x_n=%.3f%s%.3fx_{n-1},\,x_0=%.3f$' % (b,'-' if a < 0 else '+', abs(a),x0)
    
    plt.plot(terms,label=lbl)
    print terms.T, b/(1-a) if abs(a) < 1 else 'divergent'
    
    
# Calculate the equilibrium
plot_fol(20,0.999,2,-1)
plot_fol(20,1,2,-1)
plot_fol(20,1.001,2,-1)
plt.legend(loc='lower left')