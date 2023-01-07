import numpy as np
from matplotlib import pyplot as plt
import os
from conic_funcs import *

c1x, c1y = circ_gen((0,0), 5)
c2x, c2y = circ_gen((4,0), 3)
plt.plot(c1x, c1y)
plt.plot(c2x, c2y)
plt.plot([4,4],[3,-3])
plt.plot([0,4],[0,0],'k.')
plt.text(4,3,'A')
plt.text(4,-3,'B')
plt.text(0,0,'O$_1$')
plt.text(4,0,'O$_2$')
plt.grid()
plt.savefig('../figs/10_4_1.png')
os.system('termux-open ../figs/10_4_1.png')
