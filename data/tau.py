#!/usr/bin/env python3

import numpy as np, matplotlib.pyplot as plt

plt.figure(figsize=(3.75, 3))

lw = 1

from scipy.optimize import brentq
def Zcs(eta): return (1+eta+eta**2-eta**3)/(1-eta)**3
def volume_fraction(Z):
    eta = np.empty(len(Z))
    for i,z in enumerate(Z):
        eta[i] = brentq(lambda phi: Zcs(phi) - z, 0, 0.7)
    return eta

Z1, sim = np.genfromtxt('tau-sim.csv').T
Z2, sted = np.genfromtxt('tau-sted.csv').T
Z3, conf = np.genfromtxt('tau-conf.csv').T

plt.semilogy(Z1, sim, 's', mfc='None', label='simulation')
plt.semilogy(Z2, sted, 'o', mfc='None', label='STED')
plt.semilogy(Z3, conf, 'o', mfc='None', label='confocal')

#np.log(tau) = A / (Z-Z0)
#Z-Z0 = A / np.log(tau)
#Z = Z0 + A/np.log(tau)
tau_all = np.concatenate((sim,sted,conf))
Z_all = np.concatenate((Z1,Z2,Z3))
tau_all = sted
Z_all = Z2
#print(tau_all)
phi_all = volume_fraction(Z_all)
#print(phi_all)
phi0 = 0.616
phi_all = np.sort(phi_all)
select = phi_all > 0.5
A = (phi0-phi_all)*np.log(tau_all)
print(np.array((phi_all, A)).T)
A = np.average(A[select])
phi = np.linspace(0, 0.6, 100)
Z = Zcs(phi)

plt.semilogy(Z, np.exp(A/(phi0-phi)), '--', label='VFT')

phi = np.array([0.45, 0.523, 0.583, 0.598])
print(np.exp(A/(phi0-phi)))

plt.legend(loc='best')

plt.ylabel(r'$\tau_\alpha / \tau_B$')
plt.xlabel(r'$Z_\mathrm{CS}$')
plt.xlim([0, 30])
plt.show()
