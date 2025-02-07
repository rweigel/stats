import numpy as np

L = [40, 40, 40, 40, 
     60, 60, 60, 60, 60, 
     75, 75, 75, 75, 75, 75]
L = np.array(L)

N = 100000
debug = False

if N < 10:
    debug = True

two75s = np.nan*np.empty(N)
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

    is75 = np.where(L[0:3] == 75, 1, 0)
    if debug:
        print("Is element a 75?")
        print(is75)

    n75 = np.sum(is75)
    if debug:
        print("Number of 75s in first 3 of shuffle:")
        print(n75)

    two75s[i] = np.where(n75 == 2, 1, 0)

    if debug:
        print("Are there 2 75s in first 3 of shuffle?")
        print(two75s[i])


print("Simulation: P(two 75s) = %.4f; N = %d" % ( (np.sum(two75s)/N), N) )

print("Exact:      P(two 75s) = %.4f" % (9*6*5*3/(15*14*13)))

# A more compact solution is
two75s = 0
for i in range(N):
    selected = np.random.choice(L, 3)
    if np.sum( selected == 75 ) == 2:
        two75s = two75s + 1

print("Simulation: P(two 75s) = %.4f; N = %d" % (two75s/N, N) )
print("Exact:      P(two 75s) = %.4f" % (9*6*5*3/(15*14*13)))

# If np.random.shuffle() could shuffle the elements in each row or
# column of a matrix, the problem could be solved without a for loop.
# However, this feature seems not to have been implemented in NumPy. See
# https://stackoverflow.com/questions/50554272/randomly-shuffle-items-in-each-row-of-numpy-array/50554614


