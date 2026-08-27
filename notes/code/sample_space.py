# Write all possible outcomes of experiment of flipping a coin three times. Each outcome should be represented as a string of 'H' (heads) and 'T' (tails).
# That is, create sample space

if False:
  # First attempt - brute force
  a = []
  for i in ['H', 'T']:
    for j in ['H', 'T']:
      for k in ['H', 'T']:
        print(f'{i}{j}{k}')

if False:
  # Second attempt after recalling that there is an itertools library
  # that could probably simplify this code, which will be needed if
  # we want to flip the coin an arbitrary number of times.
  import itertools
  print(list(itertools.product(['H', 'T'], ['H', 'T'], ['H', 'T'])))

# Suggested by GPT-5.6-Sol with prompt "use itertools to simplify"
import itertools
for outcome in itertools.product(['H', 'T'], repeat=3):
  print(''.join(outcome))