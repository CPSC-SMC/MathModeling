# -*- coding: utf-8 -*-
"""
Hardy-Weinberg Law

@author: sbroad
"""

import numpy as np
import matplotlib.pyplot as plt

def draw_child(p):
    '''
    draw a single child
    '''
    draw = np.random.binomial(2,p)
    if draw == 0:
        return 'aa'
    elif draw == 1:
        return 'Aa'
    else:
        return 'AA'
    
def draw_children(p,size):
    '''
    draw several children
    '''
    return [draw_child(p) for i in range(size)]    
    

# no selection
# randomly select 25 children
print 'p=0.2', draw_children(0.2,25)
print 'p=0.8', draw_children(0.8,25)

# with selection (remove 'aa' and recalculate p)
A = draw_children(0.2,100)
print '100 children after selection', A