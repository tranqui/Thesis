#!/usr/bin/env python3

import numpy as np, matplotlib.pyplot as plt

c = 1
h = 1.75
V = lambda x: - 0.25 * h * x**2 + 0.5 * c * x**4
x0 = np.sqrt(0.25 * h / c)
V0 = V(x0)

x = np.linspace(-1, 1, 1000)
plt.plot(x, V(x))

plt.plot([-x0, x0], [0, 0], '--k')
#plt.plot([0, 0], [V0, 0])
plt.axhline(y=V0, ls='dashed')

#plt.arrow([x0, x0], [V0, 0], dx=1, dy=1)
plt.annotate(s='', xy=(0,0), xytext=(0,V0), arrowprops=dict(arrowstyle='<->'))

plt.text(0.075, 0.8, '$\Phi$', transform = plt.gca().transAxes)
plt.text(5e-2, 0.5*V0, '$\Delta\Phi$',
         horizontalalignment='left',
         verticalalignment='center')

plt.axis('off')
plt.show()
