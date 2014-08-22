# -*- coding: utf-8 -*-
"""
Julia sets: fractals defined by iterated functions

Created on Thu Aug 21 08:27:34 2014

@author: sbroad
"""
import numpy as np
from matplotlib.pyplot import imshow, close
import matplotlib.pyplot as plt

def julia(z,c,n=1):
    '''
    This function performs n iterations of the julia map.
    
    z ---> a complex number or array of complex numbers to map
    c ---> the Julia constant in z^2 + c
    n ---> the number of iterations
    '''
    for i in range(n):
        z = z**2 + c
    return z

def main():
    '''
    Main function for this script.
    '''
    
    '''The following four lines are items you might want to change.'''
    it = 50         # 50 iterations ... increase or decrease as desired
    c = 0.285+0.01j # a Julia constant ... pick one
    size = 1.2      # the largest real and imaginary part
    width = 1001    # number of pixels of width
    
    # Create an initial array of complex numbers, 1j is like i
    initial = np.array([[x + y*1j for x in np.linspace(-size,size,num=width)] for y in np.linspace(-size,size,num=width)])
    
    # Apply the Julia map many times. Compute the modulus of each
    #   complex number in the array
    final = abs(julia(initial,c,it))
    
    # For some initial values, the repeating the Julia map sends their
    #   values to infinity... basically once you pass 2 you're done
    #   so replace any value larger than 2 with 2
    capped = np.where(final<2,final,np.NaN) 
    
    # display a picture of the results
    close()
    imshow(capped, origin='lower')
    plt.axis('off')






# run the main function if appropriate
if __name__ == "__main__":
    main()