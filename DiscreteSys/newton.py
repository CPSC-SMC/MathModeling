# -*- coding: utf-8 -*-
"""
Newton's method

Created on Mon May 19 13:59:32 2014

@author: sbroad
"""

import numpy as np
import matplotlib.pyplot as plt

def newton(f,x,dx=0.00001,n=1):
    '''
    Update function for Newton's method
    
    f ---> the function whose roots are being computed
    x ---> the current estimate for x s.t. f(x) approx 0
    dx ---> a small value to use when approximating the derivative
    '''
    for i in range(n):
        df = (f(x+dx)-f(x-dx))/(2*dx)
        x -= f(x)/df
    return x

def main():
    # setup initial guess
    plt.close(1)
    func = lambda x: np.sin(x**2)
    xs = np.linspace(-np.pi,np.pi,101)
    plt.plot(xs,func(xs),'-')
    x = 1.5
    plt.plot(x,func(x),'o')
    for i in range(10):
        xnew = newton(func, x)
        plt.plot([x,xnew,xnew],[func(x),0,func(xnew)],'-+')
        x = xnew
    
    plt.plot(x,func(x),'o')
    print '%.5fpi is the best estimate for a root of this function' % (x/np.pi)
    
if __name__=='__main__':
    main()