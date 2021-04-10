# Plotting a matrix
import numpy as np
from matplotlib import pyplot as plt

M = np.array([[1,2,3],[4,5,6],[7,8,9]])
xc = np.arange(-1, 2) # center values for x
yc = np.arange(0, 3) # center values for y

xe = np.append(xc, 2) # Bin edges for x (columns)
xe = xe - 0.5
ye = np.append(yc, 3) # Bin edges for y (rows)
ye = ye - 0.5

plt.figure(1)
m = plt.pcolor(xe, ye, M, cmap=plt.get_cmap('viridis', 9))
# Here I've chosen the number of colors and colorbar axis limits
# so the color rectangles on the colorbar are centered on integers,
# because the data are all integer. See below for a more general case.
m.set_clim(0.5,9.5)
cb = plt.colorbar(m)
plt.ylabel('$y$')
plt.xlabel('$x$')
cb.ax.set_title('M(x,y)')

# Set ticks to match centers
plt.xticks(xc)
plt.yticks(yc)


M = np.random.normal(0, 1, size=(3,3))
cmax = np.ceil(np.max(M))   # Round up to integer
cmin = np.floor(np.min(M))  # Round down to integer
nc = np.int(2*(cmax-cmin))  # Number of colors so there will be two colors
                            # per integer step
plt.figure(2)
m = plt.pcolor(xe, ye, M, cmap=plt.get_cmap('viridis', nc))
m.set_clim(cmin,cmax)
cb = plt.colorbar(m)
plt.ylabel('$y$')
plt.xlabel('$x$')
cb.ax.set_title('M(x,y)')

# Set ticks to match centers (this will give overlapping tick labels
# if there are more than about 10 values in either array.)
plt.xticks(xc)
plt.yticks(yc)
