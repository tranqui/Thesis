#!/usr/bin/env python3

import numpy as np, matplotlib.pyplot as plt

eta_freezing = 0.494
eta_melting = 0.545
eta_rcp = 0.644
eta_cp = np.pi / (3*np.sqrt(2))

# EOS for the liquid
def Z_liquid(eta):
    return (1 + eta + eta**2 - eta**3) / (1 - eta)**3
def Z_crystal(eta):
    return Z_liquid(eta_freezing) + 1 / np.abs(eta - eta_cp) - 1 / np.abs(eta_melting - eta_cp)

N = 1000
phi_liquid = np.linspace(0, eta_freezing, N)
phi_coexistence = np.linspace(eta_freezing, eta_melting, N)
phi_crystal = np.linspace(eta_melting, eta_cp, N)
phi_metastable = np.linspace(eta_freezing, eta_rcp, N)

plt.plot(phi_liquid, Z_liquid(phi_liquid))
plt.plot(phi_coexistence, Z_liquid(np.array([eta_freezing]*N)), 'k-')
plt.plot(phi_crystal, Z_crystal(phi_crystal), 'k-')
plt.plot(phi_metastable, Z_liquid(phi_metastable), '--')

c = 'darkgrey'
plt.axvline(x=eta_freezing, ls='dashed', c=c)
plt.axvline(x=eta_melting, ls='dashed', c=c)
plt.axvline(x=eta_cp, ls='dashed', c=c)

plt.ylim([0, 40])
plt.xlim([0, 0.8])
plt.xlabel(r'$\eta$')
plt.ylabel(r'$\beta p / \rho$')

plt.show()
