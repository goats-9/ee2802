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
S = np.array([[5],[0]])
R = np.array([[7/5],[24/5]])
M = np.array([[7/5],[-24/5]])
O = np.array([[0],[0]])
line_plot(S,R)
line_plot(S,M)
line_plot(R,M)
plt.grid()
point_label(S,'R')
point_label(R,'S')
point_label(M,'M')
point_label(O,'O')
plt.savefig('../figs/10_4_5.png')
os.system('termux-open ../figs/10_4_5.png')
