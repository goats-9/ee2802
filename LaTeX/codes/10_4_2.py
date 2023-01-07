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

cx, cy = circ_gen((0,0), 5)
plt.plot(cx, cy)
A = np.array([[5],[0]])
B = np.array([[-5],[0]])
C = np.array([[-4],[3]])
D = np.array([[4],[3]])
O = np.array([[0],[0]])
E = line_intersect_pt(A,C,B,D)
line_plot(A,C)
line_plot(B,D)
line_plot(O,A)
line_plot(O,B)
line_plot(O,C)
line_plot(O,D)
plt.grid()
point_label(A,'A')
point_label(B,'B')
point_label(C,'C')
point_label(D,'D')
point_label(E,'E')
point_label(O,'O')
plt.savefig('../figs/10_4_2.png')
os.system('termux-open ../figs/10_4_2.png')
