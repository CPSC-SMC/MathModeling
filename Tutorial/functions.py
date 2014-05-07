# 
# Define and apply functions
# 

# 0. import numpy and pyplot
import numpy as np
import matplotlib.pyplot as plt

# 1. Define a function that returns the exponential of sqrt x
def func(x):
    return np.exp(np.sqrt(x))-np.e

# 2. Define another function that returns m*x+b. Make b and m the 2nd and 3rd inputs to the function
def line(x,b,m):
    return b+m*x

# 3. Create an array X of values between 0 and 2 with numpy.linspace(...). Use num=21.
A = np.linspace(0,10,num=4)

# 4. Plot each of these functions. Use a slope of 0.5 and an intercept of -1
plt.plot(A,line(A,-1,0.5))
plt.plot(A,func(A),'go-')

# 5. Define a piecewise function which has three pieces:
#       cos(x) when x < pi
#       (x-pi)**2 - 1 when pi < x < 5
#       ()
