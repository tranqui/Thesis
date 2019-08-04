#!/usr/bin/env python3

import numpy as np, matplotlib.pyplot as plt
from scipy.integrate import quad

#plt.figure(figsize=(3.375, 3))

eta = np.linspace(0.54, 0.68, 100)

f = lambda s: 1 / s**3
smax = 1 / 0.4492
A = 1 / quad(f, 1, smax)[0]
f = lambda s: A / s**3
M1 = quad(lambda s: s * f(s), 1, smax)[0]
M2 = quad(lambda s: s**2 * f(s), 1, smax)[0]
M3 = quad(lambda s: s**3 * f(s), 1, smax)[0]

rho = 6*eta / np.pi / M3
n0 = rho
n1 = rho * M1 / 2
n2 = np.pi * rho * M2
n3 = eta

# Z = (n0 / (1 - n3) + n1*n2 / (1-n3)**2 + n2**3 * (3 - n3) / (36*np.pi * (1 - n3)**3)) / rho
# plt.plot(eta, Z, '--', label='BMCSL')

Z = (n0 / (1 - n3) + 4/3 * n1*n2 / (1-n3)**2 + 2/3 * n2**3 / (12*np.pi * (1 - n3)**3) - 4*np.pi / (1-n3) * n1**2*n2 / (n2**2 + 12*np.pi * n1 * (1-n3))) / rho
plt.plot(eta, Z, '--', label='CS')

eta, Z = np.genfromtxt('swap-eos-n1000.dat').T
plt.plot(eta, Z, 'o', mew=0.5, mfc='None', label='MC N=1000')

eta, Z = np.genfromtxt('swap-eos-n8000.dat').T
plt.plot(eta, Z, '^', mew=0.5, mfc='None', ms=3.5, label='MC N=8000')

plt.legend(loc='best')
plt.xlabel(r'$\eta$')
plt.ylabel(r'$\beta p / \rho$')
plt.xlim([0.54, 0.68])
plt.ylim([15, 45])
plt.xticks(np.arange(0.54, 0.69, 0.02))
plt.yticks(np.arange(15, 46, 5))

plt.show()
