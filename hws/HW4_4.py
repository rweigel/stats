import os
import pickle
import numpy as np
from datetime import datetime

from matplotlib import pyplot as plt

def find(condition):
    return np.asarray(condition).nonzero()[0]

def read_file():

    if os.path.exists('HW4_4.pkl'):
        print('Reading ' + 'HW4_4.pkl')
        with open('HW4_4.pkl', 'rb') as f:
            return pickle.load(f)

    # TODO: Use
    # import pandas as pd
    # data = pd.read_csv(r'xray.txt', delim_whitespace=True, header = None, names = ["Year", "Month", "Day", "Hour", "Minute"])
    # data = pd.to_datetime(data)

    # pandas readcsv is a better option.
    # It is generally faster and can parse times.
    x = np.genfromtxt('xray.txt')
    x = np.asarray(x, dtype=np.int)

    T_e = []
    T_er = []
    for i in range(x.shape[0]):
        t_e = datetime(x[i,0],x[i,1],x[i,2],x[i,3],x[i,4])
        T_e.append(t_e)

        t_er = t_e - datetime(x[0,0],x[0,1],x[0,2],0,0)
        t_er = np.floor(t_er.total_seconds()/3600)
        T_er.append(t_er)

    with open('HW4_4.pkl', 'wb') as f:
        print('Saving ' + 'HW4_4.pkl')
        pickle.dump(T_er, f)

    return T_er

T_er = read_file()

E = np.zeros(int(T_er[-1]+1))
T = np.arange(int(T_er[-1]+1))
T_er = np.array(T_er, dtype=np.int)
E[T_er] = 1

#plt.plot(T/24, E)
#plt.xlabel('Days since 2000-01-01')

idx_f = find(E == 1)
idx_fbar = find(E == 0)

n11 = np.logical_and(E[0:-1] == 1, E[1:] == 1).nonzero()[0].size
n10 = np.logical_and(E[0:-1] == 1, E[1:] == 0).nonzero()[0].size
n00 = np.logical_and(E[0:-1] == 0, E[1:] == 0).nonzero()[0].size
n01 = np.logical_and(E[0:-1] == 0, E[1:] == 1).nonzero()[0].size

p   = idx_f.size/E.size
p11 = n11/E.size
p10 = n10/E.size
p00 = n00/E.size
p01 = n01/E.size

print("P(F)             = %.4f" % p)
print("P(F_t|F_{t-1})   = %.4f" % p11)
print("P(F_t|xF_{t-1})  = %.4f" % p10)
print("P(xF_t|xF_{t-1}) = %.4f" % p00)
print("P(xF_t|F_{t-1})  = %.4f" % p01)

#print(a.size,b.size,c.size,d.size)
