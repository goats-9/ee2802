import numpy as np
import matplotlib.pyplot as plt
import os

#Generating points on a parabola
def parab_gen(x,a):
	y = x**2/a
	return y

X = np.linspace(-8,8,10000)
a = 25/2
plt.plot(X,parab_gen(X,a))
plt.grid()
plt.tight_layout()
plt.savefig('../figs/conic.png')
os.system('termux-open ../figs/conic.png')
