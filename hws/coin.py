#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 12:10:35 2021

@author: weigel
"""

import numpy as np

Nt = 10

x = np.random.randint(0, 2, size=(Nt,3))

print('x = ')
print(x)

tf = (x[:,0] == 1) & (x[:,1] == 1) & (x[:,2] == 1)
print('tf = ')
print(tf)

idx = np.where(tf)

print('idx = ')
print(idx[0])

print(x[idx,:])



