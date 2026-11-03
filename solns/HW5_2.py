from lib import dft

y = [0, 1, 0, -1]
a0, a, b, i, f = dft.dft(y, method='slow')
dft.print(a0, a, b, i, f)
