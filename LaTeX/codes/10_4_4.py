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

c1x, c1y = circ_gen((0,0), 3*np.sqrt(2))
c2x, c2y = circ_gen((0,0), 5)
plt.plot(c1x, c1y)
plt.plot(c2x, c2y)
A = np.array([[-4],[3]])
B = np.array([[-3],[3]])
C = np.array([[3],[3]])
D = np.array([[4],[3]])
E = np.array([[0],[3]])
O = np.array([[0],[0]])
line_plot(A,D)
line_plot(O,E)
point_label(A,'A')
point_label(B,'B')
point_label(C,'C')
point_label(D,'D')
point_label(E,'E')
point_label(O,'O')
plt.grid()
plt.savefig('../figs/10_4_4.png')
os.system('termux-open ../figs/10_4_4.png')
