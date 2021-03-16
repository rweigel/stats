#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 11:31:06 2021

@author: weigel
"""

import numpy as np

for i in range(1000):
    np.random.seed(i)
    x = np.random.normal(130.0, 1.5, size=9)
    xm = np.mean(x)
    if 131.075 <= xm <= 131.085:
        print(i,np.mean(x))


np.random.seed(623)
x = np.random.normal(130.0, 1.5, size=9)
print(np.mean(x)) #131.0812930740811

