#!/usr/bin/env python3

import numpy as np, matplotlib.pyplot as plt

plt.figure(figsize=(3.75, 3))

lw = 1

Z1, sim = np.genfromtxt('tau-sim.csv').T
Z2, sted = np.genfromtxt('tau-sted.csv').T
Z3, conf = np.genfromtxt('tau-conf.csv').T

plt.semilogy(Z1, sim, 's', mfc='None', label='simulation')
plt.semilogy(Z2, sted, 'o', mfc='None', label='STED')
plt.semilogy(Z3, conf, 'o', mfc='None', label='confocal')
plt.legend(loc='best')

plt.ylabel(r'$\tau_\alpha / \tau_B$')
plt.xlabel(r'$Z_\mathrm{CS}$')
plt.xlim([0, 30])
plt.show()
