# -*- coding: utf-8 -*-
"""

Created on Fri Oct 17 10:00:49 2014

@author: sbroad
"""

import numpy as np
import matplotlib.pyplot as plt


def empirical_cdf(xvals,data=np.random.random(50)):
    """
    Compute the cumulative probabilities of possible outcomes of a random 
    variable, given an empirical data set as the basis of an empirical
    cumulative distribution function.
    
    xvals --> The values for which cumulative probabilities are required.
              May be a multidimensional array.
    data --> The empirical data on which to base these probabilities.
             Default value: 50 observations from a uniform random variable on
             the interval [0,1]
             
    Note: this function is designed to be plot-able i.e., if x is a vector of
    input values, and d is an empirical data set, then
    
    plot(x, empirical_cdf(x,d))
    
    produces a plot of the empirical CDF.
    """
    n = float(np.size(data)) # determine the size of the empirical data
    
    # copy and flatten the input value array. we will reshape it later.
    cdfvals = np.copy(xvals).flatten() 
    
    # compute the empirical cumulative probability for each input value
    for i in range(len(cdfvals)):
        
        # first we need to know how many empirical data points are less than
        # the input value
        ks = np.where(data<cdfvals[i])
        
        # the cumulative empirical probability is the proportion of the 
        # data points that are less than or equal to the input value
        cdfvals[i] = np.size(ks)/n
        
    # we have now computed all cumulative probabilities
    # return the reshaped cumulative probability array
    return np.reshape(cdfvals,np.shape(xvals))
    

'''
Example: obtain the general shape of the cdf of a normal random variable.

Mean = 0, Standard Deviation = 1

Use 100 different empirical data sets to generate pictures of the cdfs.
'''
d = np.random.binomial(n=2, p=0.50, size=50)
xs = np.linspace(-1,3,1001)
plt.plot(xs,empirical_cdf(xs,data=d),'.')
