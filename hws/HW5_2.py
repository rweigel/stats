import os
import pickle
import numpy as np
from datetime import datetime

from matplotlib import pyplot as plt
base_name = 'HW5_2'

def find(condition):
    return np.asarray(condition).nonzero()[0]

def read_file():

    pkl_file = base_name + '.pkl'
    if os.path.exists(pkl_file):
        print('Reading ' + pkl_file)
        with open(pkl_file, 'rb') as f:
            return pickle.load(f)

    if not os.path.exists('xray.txt'):
        import urllib.request
        xurl = "http://mag.gmu.edu/git-data/astrostats/SOLAR_FLARES/xray.txt"
        urllib.request.urlretrieve(xurl, "xray.txt")

    if False:
        # TODO: Use pandas because it can parse times.
        import pandas as pd
        names = ["Year", "Month", "Day", "Hour", "Minute"]
        data = pd.read_csv(r'xray.txt', delim_whitespace=True, header=None, names=names)
        data = pd.to_datetime(data)

    x = np.genfromtxt('xray.txt')
    x = np.asarray(x, dtype=np.int_)

    T_e = []
    T_er = []
    for i in range(x.shape[0]):
        t_e = datetime(x[i,0],x[i,1],x[i,2],x[i,3],x[i,4])
        T_e.append(t_e)

        t_er = t_e - datetime(x[0,0],x[0,1],x[0,2],0,0)
        t_er = np.floor(t_er.total_seconds()/3600)
        T_er.append(t_er)

    with open(pkl_file, 'wb') as f:
        print('Saving ' + pkl_file)
        pickle.dump(T_er, f)

    return T_er

T_er = read_file()

E = np.zeros(int(T_er[-1]+1))
T = np.arange(int(T_er[-1]+1))
T_er = np.array(T_er, dtype=np.int_)
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
