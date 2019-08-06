#!/usr/bin/env python3

import numpy as np, matplotlib.pyplot as plt

#eta_freezing = 0.494
#eta_melting = 0.545
eta_freezing = np.pi / 6 * 0.943
eta_melting = np.pi / 6 * 1.04
eta_rcp = 0.644
#sys.exit(0)
eta_cp = np.pi / (3*np.sqrt(2))

plt.figure(figsize=(3.375, 2.75))
c = [next(plt.gca()._get_lines.prop_cycler)['color'] for _ in range(3)]

def draw_phase_boundaries():
    xlim = plt.gca().get_xlim()
    ylim = plt.gca().get_xlim()
    plt.text(eta_freezing - 5e-3, 39, 'freezing',
             horizontalalignment='right', verticalalignment='top',
             rotation='vertical')
    # plt.text(0.5 * (eta_melting + eta_freezing), 39, 'coexistence',
    #          horizontalalignment='center', verticalalignment='top',
    #          rotation='vertical')
    plt.text(eta_melting + 15e-3, 39, 'melting',
             horizontalalignment='left', verticalalignment='top',
             rotation='vertical')
    plt.text(eta_cp + 15e-3, 39, 'close packing',
             horizontalalignment='left', verticalalignment='top',
             rotation='vertical')
    plt.text(0.5*eta_freezing, 12, 'fluid',
             horizontalalignment='center', verticalalignment='center')
    plt.text(0.5*(eta_melting + eta_cp), 1, 'crystal',
             horizontalalignment='center', verticalalignment='bottom')
    #plt.axvspan(freezing, melting, alpha=0.5, color='b', lw=0., hatch='\\\\\\')
    c1 = np.array([1,1,1])
    c2 = np.array([1,1,0.75])
    plt.axvspan(0, eta_melting, color=c1, ec='none')
    plt.axvspan(eta_melting, xlim[-1], color=c2, ec='none')

    X = np.linspace(eta_freezing,eta_melting,11)[:-1]
    dx = X[1] - X[0]
    for i,x in enumerate(X):
        cc = (i*c2 + (len(X)-1-i)*c1) / (len(X)-1)
        plt.axvspan(x, x+dx, color=cc, ec='none')

    plt.xlim(xlim)

# EOS for the liquid
def Z_liquid(eta):
    return (1 + eta + eta**2 - eta**3) / (1 - eta)**3
def Z_crystal(eta, a=0.620735, b=0.708104, c=0.591663):
    z = eta_melting / eta_cp
    Zm = 3 / (1 - z) - a * (z-b) / (z-c)
    z = eta / eta_cp
    Z = 3 / (1 - z) - a * (z-b) / (z-c)
    return Z - Zm + Z_liquid(eta_freezing)

N = 1000
phi_liquid = np.linspace(0, eta_freezing, N)
phi_coexistence = np.linspace(eta_freezing, eta_melting, N)
phi_crystal = np.linspace(eta_melting, eta_cp, N)
phi_metastable = np.linspace(eta_freezing, eta_rcp, N)

plt.plot(phi_liquid, Z_liquid(phi_liquid), c=c[0], label='equilibrium')
plt.plot(phi_metastable, Z_liquid(phi_metastable), '--', c=c[1], label='metastable')
plt.legend(loc='best')

plt.plot(phi_coexistence, Z_liquid(np.array([eta_freezing]*N)), 'k-')
plt.plot(phi_crystal, Z_crystal(phi_crystal), 'k-')

cl = 'darkgrey'
cl = c[2]
plt.axvline(x=eta_freezing, ls='dashed', c=cl)
plt.axvline(x=eta_melting, ls='dashed', c=cl)
plt.axvline(x=eta_cp, ls='dashed', c=cl)

plt.ylim([0, 40])
plt.xlim([0, 0.81])
plt.xlabel(r'$\eta$')
plt.ylabel(r'$\beta p / \rho$')

draw_phase_boundaries()

plt.show()
