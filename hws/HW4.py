#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 16:34:38 2021

@author: weigel
"""
import numpy as np

x = np.random.binomial(24000, 9/240)

# Inpect every 24 values, count number of 1s

# 1000 rows like

# 0 0 0 0 0 1 0 0 => Nevents = 1
# 0 1 0 0 0 1 0 0 => Nevents = 2
# ...
# 0 0 0 0 0 0 1 0 => Nevents = 1



