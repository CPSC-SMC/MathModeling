# -*- coding: utf-8 -*-
"""
Basins of attraction

Created on Sun Jun  1 15:22:25 2014

@author: sbroad
"""

from logistic import *
from newton import *

# investigate the basin of attraction for each of several logistic parameters
init = np.random.random(200)

plt.close(1)
plt.figure(1)
for a in [(0.5,'b.'), (1.5,'g.'), (2.5,'r.'), (3.2,'k.')]:
    attr = [ logistic(x, a[0], n=100) for x in init]
    plt.plot(init, attr,a[1],label=r'$\lambda=%.2f$' % (a[0]))

plt.ylim(ymin=0,ymax=1)
plt.legend(loc='best')

# investigate the basin of attraction for roots of sin(x)
init = np.random.random(200)*10

plt.close(2)
plt.figure(2)
quad = (lambda x: x**2-6*x+8, 'b.', r'$x^2-5x+4$')
trig = (lambda x: sin(x/2.), 'g.', r'$\sin(\pi x)$')
tran = (lambda x: log(x),'r.', r'$\log x$')
for b in [quad, trig, tran]:
    attr = [newton(b[0], x, n=100) for x in init]
    plt.plot(init, attr, b[1], label=b[2])

plt.legend(loc='best')