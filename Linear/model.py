# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 08:09:03 2014

@author: Steven
"""

import numpy as np
import matplotlib.pyplot as plt

def linear_model(x,b):
    print len(x), len(b)
    assert(len(x)==len(b)-1)
    x = np.concatenate((np.array([1]),x))
    return dot(x,b)
    
print linear_model(np.array([1,1,1]),np.array([4,1,-3,6]))