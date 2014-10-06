# -*- coding: utf-8 -*-
"""
Accelerometer app data

@author: sbroad
"""

import numpy as np
import matplotlib.pyplot as plt

class Accelerometer:
    def __init__(self, filename):
        self.filename = filename
        self.load_data()
        
    def load_data(self, filename = ""):
        if len(filename) > 0:
            self.filename = filename
        
        elif len(self.filename) == 0:
            raise Exception('Data cannot be loaded. No file specified.')
        
        f = open(self.filename)
        
        self.cols = f.readline().replace('\x00','').split(',')

        data = []
        
        for line in f.readlines():
            nxt = np.array([float(v) for v in line.split(',')])
            data.append(nxt)

        self.data = np.array(data)
        
        f.close()

    def get_col(self,col,tmin=0,tmax=1e10):
        if type(col) == str:
            i = self.cols.index(col)
        else:
            i = col
        
        return self.get_time_range(tmin, tmax)[:,i]
    
    def get_time_range(self, tmin=0, tmax=1e10):
        return np.array(filter(lambda x: tmin <= x[0] <= tmax, self.data))
    
    def crop_range(self, tmin, tmax):
        self.data = self.get_time_range(tmin, tmax)
        
    def get_time(self, tmin=0, tmax=1e10):
        return self.get_col('TIME', tmin, tmax)
    
    def get_x(self, tmin=0, tmax=1e10):
        return self.get_col('X', tmin, tmax)
    
    def get_y(self, tmin=0, tmax=1e10):
        return self.get_col('Y', tmin, tmax)
    
    def get_z(self, tmin=0, tmax=1e10):
        return self.get_col('Z', tmin, tmax)
            
    def get_a(self, tmin=0, tmax=1e10):
        return np.sqrt(self.get_x(tmin, tmax)**2 + self.get_y(tmin, tmax)**2 + self.get_z(tmin, tmax))
        
        
def main():
    a = Accelerometer('driving.txt')

    plt.plot(a.data[:,0],a.get_a())
    plt.xlabel(u'Time, $t$ (s)')
    plt.ylabel(u'Acceleration, $a$ (Gravities, i.e. $1=-9.8m/s^2$)')

# run the main function if appropriate
if __name__ == "__main__":
    main()