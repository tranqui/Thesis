#!/usr/bin/env python3

import numpy as np, matplotlib.pyplot as plt

#plt.figure(figsize=(3.75, 3.75))
plt.figure(figsize=(3.75, 3))

lw = 1

r, D = np.genfromtxt('g2-045.csv').T
plt.plot(r, D, lw=lw, label=r'$\eta = 0.45$')

_,r,A,B,C = np.genfromtxt('g2-hallett.txt', skip_header=1).T
plt.plot(r, A+1, lw=lw, label='0.523')
plt.plot(r, B+1, lw=lw, label='0.583')
plt.plot(r, C+1, lw=lw, label='0.598')

plt.legend(loc='best', ncol=2)
plt.xlim([0, 5])

plt.xlabel('$r / \sigma$')
plt.ylabel('$g^{(2)}(r)$')

plt.show()
