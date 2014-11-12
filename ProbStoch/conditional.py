# -*- coding: utf-8 -*-
"""
Computing conditional probabilities

Created on Wed Nov 12 11:00:29 2014

@author: sbroad
"""

import numpy as np
import matplotlib.pyplot as plt

# obtain your data
data = np.genfromtxt('KidCreative.csv',delimiter=',')

# obtain your data columns
buy = data[1:,1] # the buy column
reslen = data[1:,9] # the residence length column
female = data[1:,3] # the is female column

"""
# method 1 : np.where

# A = person buys the magazine
# B = person has lived in their residence for more than 10 years
# C = person is female
"""

print 'Method 1: np.where'
# list of A
buyY, = np.where(buy==1) # a list of the element positions where buy is 1
print 'n(A) =', np.size(buyY)

# list of A and B
buyYover10 = buyY[np.where(reslen[buyY]>10)]
print 'n(A and B) =', np.size(buyYover10)

# compute P(B|A) = P(A and B) / P(A) = n(A and B) / n(A)
print 'P(B|A) =', float(np.size(buyYover10))/np.size(buyY)

# list of not C i.e., female==0
femaleN, = np.where(female==0)
print 'n(not C) =', np.size(femaleN)

# list of B  and not C
male_over10 = femaleN[np.where(reslen[femaleN]>10)]
print 'n(B and not C) = ', np.size(male_over10)

# list of A and B and not C
buy_male_over10 = male_over10[np.where(buy[male_over10]==1)]
print 'n(A and B and not C) =', np.size(buy_male_over10)

# compute P(A | B and not C) = n(A and B and not C) / n(B and not C)
print 'P(A|B and not C) =', float(np.size(buy_male_over10))/np.size(male_over10)
print

"""
# method 2 : logical operators

# A = person buys the magazine
# B = person has lived in their residence for more than 10 years
# C = person is female
"""

print 'Method 2: Logical operators'

# list of A
buyY = buy==1
print 'n(A) =', np.sum(buyY)

# list of A and B, "and" represented by * ("or" is represented by +)
over10 = reslen>10
print 'n(A and B) =', np.sum(over10 * buyY)

# compute P(B|A) = P(A and B) / P(A) = n(A and B) / n(A)
print 'P(B|A) =', float(np.sum(over10 * buyY))/np.sum(buyY)

# list of not C
femaleN = female==0
print 'n(not C) =', np.sum(femaleN)

# list of B
over10 = reslen>10
print 'n(B and not C) =', np.sum(femaleN * over10)

# list of A and B and not C
buyY = buy==1
print 'n(A and B and not C) =', np.sum(buyY * over10 * femaleN)

# compute P(A | B and not C) = n(A and B and not C) / n(B and not C)
print 'P(A|B and not C) =', float(np.sum(femaleN * over10 * buyY))/np.sum(femaleN * over10)

