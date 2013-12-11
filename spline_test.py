# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 14:05:26 2013

@author: katia
"""
from matplotlib import pyplot
import matplotlib.pyplot as plt
import numpy
import math
from scipy.interpolate import interp1d
from scipy.interpolate import UnivariateSpline

import numpy as np
import scipy as sp
from scipy.interpolate import interp1d

def moving_average(x, y, N=1):
    y_new = y
    for jj in xrange(N,len(y)-N):
        print jj-N
        y[jj-N], 1111111111
        a = jj - N
        b = jj+N
        print y[a]
        print y[a:b]
        #print y[(jj-N):(jj+N)]
        y_new[jj] = sum(y[a:b])/float(len(y[a:b]))
    print y_new
    return x, y_new

#x = [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 171, 172, 173, 174, 177, 178]
#y = [1, 2, 1, 1, 4, 3, 4, 4, 3, 1, 3, 5, 3, 8, 4, 5, 7, 7, 6, 8, 10, 8, 6, 8, 11, 12, 13, 12, 15, 12, 9, 12, 6, 12, 8, 8, 11, 16, 12, 14, 10, 17, 14, 14, 13, 4, 14, 15, 10, 15, 9, 7, 19, 14, 9, 8, 19, 13, 12, 7, 20, 14, 9, 11, 14, 11, 15, 12, 14, 8, 10, 16, 12, 10, 9, 7, 18, 5, 9, 8, 16, 8, 11, 8, 9, 7, 5, 8, 7, 3, 7, 8, 5, 7, 6, 8, 5, 7, 1, 1, 2, 5, 4, 5, 6, 2, 2, 4, 4, 5, 3, 2, 2, 1, 4, 3, 3, 3, 2, 1, 2, 1, 1]

x = [1,2,3,4,5]
y = [10, 15, 13, 18,10]

#xnew = x
##plt.plot(x_ax, y_ax,'o',xnew, f2(xnew),'--')
##plt.show()
#
#s = UnivariateSpline(x, y, s=1)
#xs = x
#ys = s(xs)
x, y_new = moving_average(x, y)
plt.plot(x, y, '.-')
plt.plot(x, y_new, "y*")
#plt.plot(xs, ys)
#plt.show()