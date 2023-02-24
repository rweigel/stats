import numpy as np

L = [0, 0, 0, 0, 
     1, 1, 1, 1, 1, 
     2, 2, 2, 2, 2, 2]
L = np.array(L)

N = 100000
debug = False

if N < 10:
    debug = True

twoReds = np.nan*np.empty(N)
for i in range(N):
    if debug:
        print('-'*50)
        print('Shuffle # %d/%d' % (i,N))
        print('-'*50)
    np.random.shuffle(L)
    if debug:
        print("Shuffle of bulbs:")
        print(L)
        print("First 3 of shuffle:")
        print(L[0:3])

    isRed = np.where(L[0:3] == 0, 1, 0)
    nRed = np.sum(isRed)
    if debug:
        print("Number of reds in first 3 of shuffle:")
        print(nRed)

    twoReds[i] = np.where(nRed == 2, 1, 0)

    if debug:
        print("Are there 2 reds in first 3 of shuffle?")
        print(twoReds[i])


print("Simulation: P(two reds) = %.4f; N = %d" % ( (np.sum(twoReds)/N), N) )

print("Exact:      P(two reds) = %.4f" % (3*(4*3*5+4*3*6)/(15*14*13)))

# A more compact solution is
twoReds = 0
for i in range(N):
    selected = np.random.choice(L, 3, replace=False)
    if np.sum( selected == 0 ) == 2:
        twoReds = twoReds + 1

print("Simulation: P(two reds) = %.4f; N = %d" % (twoReds/N, N) )
print("Exact:      P(two reds) = %.4f" % (3*(4*3*5+4*3*6)/(15*14*13)))

# If np.random.shuffle() could shuffle the elements in each row or
# column of a matrix, the problem could be solved without a for loop.
# However, this feature seems not to have been implemented in NumPy. See
# https://stackoverflow.com/questions/50554272/randomly-shuffle-items-in-each-row-of-numpy-array/50554614
