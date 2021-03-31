#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 06:38:19 2021

@author: weigel
"""
import numpy as np
from matplotlib import pyplot as plt

def count(condition):
    return np.sum(condition)

N_E = 10000
ps = np.arange(0, 1.1, 0.1)
N_T = 3 # Number of tosses/experiment
N_H = 2 # Number of heads in an experiment
n_B = np.full(ps.size, np.nan)
for i in range(ps.size):
    x = np.random.binomial(N_T, ps[i], size=N_E)
    n_B[i] = count(x == N_H)
print(n_B)

p_B = n_B/N_E
plt.bar(ps, p_B, width=0.09)
plt.xlabel('$p_{H}$ of coin')
plt.ylabel('P(experiment yields 2 heads)')
plt.title('Experiment: Toss coin having $p_H$ 3 times\nEach bin is result from 10k reps of experiment with different $p_H$')
plt.xticks(ps)

P_H = 0.5
n_H = np.random.binomial(3, P_H, size=N_E)

plt.figure()
binsc = np.arange(0, N_T + 2)
n_F, _ = np.histogram(n_H, bins=binsc-0.5)
plt.bar(binsc[0:-1]/N_T, n_F/N_E, width=0.3)
plt.xticks(binsc[0:-1]/N_T)
plt.xlabel('$F_H$ (fraction of heads in experiment)')
plt.ylabel('$P(F_H)$')
plt.title('Experiment: Toss coin having $p_H=0.5$ 3 times\nAll bins represent results from 10k experiments')
#plt.xticks(ps)