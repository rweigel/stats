import os
from matplotlib import pyplot as plt

#print(__file__)

drive, path = os.path.split(__file__)

#print(drive)
#print(path)

plt.plot(1,1)

print("Saving " + os.path.join(drive, 'myfig1.png'))
plt.savefig(os.path.join(drive, 'myfig1.png'))

print("Saving " + 'myfig2.png')
plt.savefig('myfig2.png')