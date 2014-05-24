# -*- coding: utf-8 -*-
"""
Created on Mon May 19 14:00:12 2014

@author: sbroad
"""

import matplotlib.pyplot as plt

def predprey(x,y,a,b,c,d):
    xnew = (1+a)*x - b*y*x
    ynew = -c*y + d*x*y
    return (xnew,ynew)

x = 1000.
y = 10.
a = 1.
b = 0.025
c = 1.
d = 0.005

for i in range(10):
    print x,y
    plt.plot(i,x,'ro-')
    plt.plot(i,y,'bo-')
    (x,y) = predprey(x,y,a,b,c,d)