import numpy as np
import matplotlib.pyplot as plt

A = np.loadtxt('training_data.txt')
X = np.hstack((A[:,[1]],np.ones((A.shape[0],1))))
Y = A[:,[0]]

#Least squares method
m, c = np.linalg.lstsq(X, Y, rcond=None)[0]
print(m, c)

#Plot both the results
plt.plot(X, m*X+c)
plt.plot(A[:,[1]], Y, 'k.')
plt.grid()
plt.xlabel('Output Voltage (V)')
plt.ylabel('Temperature ($^{\circ}$C)')
plt.xlim([1.6,2.0])
plt.ylim([0,70])
plt.tight_layout()
plt.savefig('../figs/train.png')

#Close current figure(s)
plt.close('all')

#Plot for validation
B = np.loadtxt('validation_data.txt')
Xv = np.hstack((B[:,[1]],np.ones((B.shape[0],1))))
Yv = B[:,[0]]
plt.plot(Xv, m*Xv+c)
plt.plot(B[:,[1]], Yv, 'k.')
plt.xlabel('Output Voltage (V)')
plt.ylabel('Temperature ($^{\circ}$C)')
plt.xlim([1.6,2.0])
plt.ylim([0,70])
plt.grid()
plt.tight_layout()
plt.savefig('../figs/valid.png')
