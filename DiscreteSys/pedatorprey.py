# -*- coding: utf-8 -*-
"""
Created on Mon May 19 14:00:12 2014

@author: sbroad
"""

import matplotlib.pyplot as plt

def predprey(x,y,a,b=0.001,c=0.01,d=0.01):
    xnew = a*x - b*y*x
    ynew = -c*y + d*x*y
    return (max(xnew,0),max(ynew,0))

x = 100
y = 50
a = 1.10081

plt.close()
for i in range(200):
    print x,y
    plt.plot(i,x,'ro-')
    plt.plot(i,y,'bo-')
    (x,y) = predprey(x,y,a)