import numpy as np
import os
from matplotlib import pyplot as plt
from conic_funcs import *
from line_funcs import *

#Macro to plot line given endpoints
def line_plot(A,B):
    plt.plot([A[0][0], B[0][0]], [A[1][0], B[1][0]], 'k')

#Macro to plot a point with text
def point_label(A,s):
    plt.plot(A[0][0],A[1][0],'k.')
    plt.text(A[0][0],A[1][0],s)

#Function that returns Cartesian coordinates
#given the corresponding Polar coordinates
def polar_to_rect(r,theta):
    return np.array([[r*np.cos(theta)], [r*np.sin(theta)]])

r = 20
t1 = 0
t2 = 2*np.pi/3
t3 = 2*t2
cx, cy = circ_gen((0,0),r)
plt.plot(cx, cy)
A=polar_to_rect(r,t1)
D=polar_to_rect(r,t2)
S=polar_to_rect(r,t3)
O = np.array([[0],[0]])
line_plot(A,D)
line_plot(D,S)
line_plot(A,S)
plt.grid()
point_label(A,'A')
point_label(D,'D')
point_label(S,'S')
point_label(O,'O')
line_plot(A,O)
line_plot(S,O)
line_plot(D,O)
plt.savefig('../figs/10_4_6.png')
os.system('termux-open ../figs/10_4_6.png')
