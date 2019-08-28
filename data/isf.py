#!/usr/bin/env python3

import numpy as np, matplotlib.pyplot as plt
import matplotlib.cm as cm

plt.figure(figsize=(3.375, 2.75))

t = np.logspace(-2, 7, 1000)

A = 0.8
B = 0.05
F = lambda a, b, d, t1, t2, t3: (1-A-B)*np.exp(-(t/t1)**a) + B*np.exp(-(t/t3)**d) + A*np.exp(-(t/t2)**b)
#F = lambda a, b, t1, t2: (1-A)*np.exp(-(t/t1)**a) + A*np.exp(-(t/t2)**b)

rainbow = cm.get_cmap('rainbow')

N = 8
T2 = np.logspace(0, 4, N)
T1 = np.linspace(1, 2, N)
T3 = np.logspace(0, 1, N)
bb = reversed(np.linspace(0.8, 2, N))
dd = reversed(np.linspace(0.8, 2, N))
cc = reversed(np.linspace(0, 1, N))
for t1,t2,t3, b,d,color in zip(T1,T2,T3, bb,dd,cc):
    plt.semilogx(t, F(2, b, d, t1, t2, t3), c=rainbow(color))

plt.text(50, 0.9, r'$\beta$-relaxation',
         horizontalalignment='left', verticalalignment='center')
plt.text(5e5, 0.75, r'$\alpha$-relaxation',
         horizontalalignment='center', verticalalignment='center')
plt.annotate(s='', xy=(2,0.9), xytext=(40,0.9), arrowprops=dict(arrowstyle='->'))
plt.annotate(s='', xy=(3e3,0.6), xytext=(5e5,0.7), arrowprops=dict(arrowstyle='->'))

plt.text(0.05, 0.5, 'normal',
         horizontalalignment='center', verticalalignment='top')
plt.text(0.05, 0.425, 'liquid',
         horizontalalignment='center', verticalalignment='top')
plt.text(5e5, 0.5, 'supercooled',
         horizontalalignment='center', verticalalignment='top')
plt.text(5e5, 0.425, 'liquid',
         horizontalalignment='center', verticalalignment='top')
plt.annotate(s='', xy=(0.25,0.15), xytext=(75000,0.15), arrowprops=dict(arrowstyle='->'))
plt.text(0.2, 0.15, '$T$',
         horizontalalignment='right', verticalalignment='center')

plt.ylim([0, 1])

plt.xlabel('time $t$')
plt.ylabel('$F(k,t) / S(k)$')
plt.show()
