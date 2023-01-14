import numpy as np
import matplotlib.pyplot as plt
import os

plt.style.use('_mpl-gallery')

#Points
P = np.array([[1.0],[2.0],[3.0]])
Q = np.array([[4.0],[5.0],[6.0]])

#Direction vectors
A = np.array([[1.0],[-3.0],[2.0]])
B = np.array([[2.0],[3.0],[1.0]])

#Arrays for plotting
M = np.hstack((P-2*A,P+2*A))
N = np.hstack((Q-2*B,Q+2*B))

# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.scatter(M[0], M[1], M[2])
ax.plot(M[0], M[1], M[2])
ax.scatter(N[0], N[1], N[2])
ax.plot(N[0], N[1], N[2])
ax.plot(P[0][0],P[1][0],P[2][0],'k.')
ax.text(P[0][0],P[1][0],P[2][0],'P')
ax.plot(Q[0][0],Q[1][0],Q[2][0],'k.')
ax.text(Q[0][0],Q[1][0],Q[2][0],'Q')
plt.grid()
plt.tight_layout()
plt.savefig('../figs/plot_3d.png', dpi=600)
os.system('termux-open ../figs/plot_3d.png')
