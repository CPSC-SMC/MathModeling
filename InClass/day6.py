# -*- coding: utf-8 -*-
"""
Genetic simulation

@author: sbroad
"""

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
    
    return value is the number of dominant alleles
    '''
    return np.random.binomial(2,p)
    
def draw_children(p,size):
    '''
    draw several children
    '''
    return np.array([draw_child(p) for i in range(size)])
    

size = 1000
print 'no selection'
print 'randomly select',size,'children'
children = draw_children(0.2,size)
print 'p0=0.2', 'p1=', sum(children)/2./len(children)
children = draw_children(0.8,size)
print 'p0=0.8', 'p1=', sum(children)/2./len(children)

# with selection (remove 'aa' and recalculate p)
print 'with selection'
print 'randomly select',size,'children'
children = draw_children(0.2,size)
survivors = filter(lambda x: x != 0, children)
print 'p0=0.2', 'p1=', sum(survivors)/2./len(survivors)

children = draw_children(0.8,size)
survivors = filter(lambda x: x != 0, children)
print 'p0=0.8', 'p1=', sum(survivors)/2./len(survivors)

children = draw_children(0.7,size)
survivors = filter(lambda x: x != 0, children)
print 'p0=0.7', 'p1=', sum(survivors)/2./len(survivors)

