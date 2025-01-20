# See also https://python.land/python-data-types/python-set

set1 = {1, 2, 3}
set2 = {2, 3, 4}

# See https://www.pythonmorsels.com/every-dunder-method/
print(dir(set1))

print(10*"-")
print("Set Operations")

print(f"set1 = {set1}")
print(f"set2 = {set2}")

# Intersection (and)
print("Intersection")
print(f" set1 ∩ set2 = {set1.intersection(set2)} (using set1.intersection(set2))")
print(f" set1 ∩ set2 = {set1 & set2} (using set1 & set2)")
# {2, 3}

# Disjoint
print("Disjoint")
print(f" set1 ∩ set2 = ϕ: {set1.isdisjoint(set2)} (using set1.isdisjoint(set2))")
# True

# Union (or)
print("Union")
print(f" set1 ∪ set2 = {set1.union(set2)} (using set1.union(set2))")
print(f" set1 ∪ set2 = {set1 | set2} (using set1 | set2)")
# {1, 2, 3, 4}

# Difference (elements that are in set1 but not in set2)
print("Difference")
print(f" set1 - set2 = {set1.difference(set2)} (using set1.difference(set2))")
print(f" set1 - set2 = {set1 - set2} (using set1 - set2)")
# {1}

# Difference (elements that are in set1 but not in set2)
print(f" set2 - set1 = {set2.difference(set1)} (using set2.difference(set1))")
print(f" set2 - set1 = {set2 - set1} (using set2 - set1)")
# {4}

# Symmetric Difference (XOR; elements that are in set1 or set2 but not in both)
# or the set of elements in precisely one of s1 or s2
print("Symmetric Difference (XOR)")
print(f" set1 ⊕ set2 = {set1.symmetric_difference(set2)} (using set1.symmetric_difference(set2))")
print(f" set1 ⊕ set2 = {set1 ^ set2} (using set1 ^ set2)")
print(f" set2 ⊕ set1 = {set2.symmetric_difference(set1)} (using set2.symmetric_difference(set1))")
print(f" set2 ⊕ set2 = {set2 ^ set1} (using set2 ^ set1)")
# {1, 4}

# Equal
print("Equal")
print(f" s1 = s2: {set1 == set2} (using set1 == set2)")

# Not equal
print("Not Equal")
print(f" s1 ≠ s2: {set1 != set2} (using set1 != set2)")

# Proper subset: s1 is subset of s2 and s1 != s2
print("Proper subset")
print(f" s1 ⊂ s2: {set1 < set2} (using set1 < set2)")

# Improper subset s1 is proper subset of s2 or s1 = s2
print("Improper subset")
print(f" s1 ⊆ s2: {set1.issubset(set2)} (using set1.issubset(set2))")
print(f" s1 ⊆ s2: {set1 <= set2} (using set1 <= set2)")

# Proper superset: s1 is superset of s2 and s1 != s2
print("Proper superset")
print(f" s1 ⊃ s2: {set1 > set2} (using set1 > set2)")

# Improper superset: s1 is proper superset of s2 or s1 = s2
print("Improper superset")
print(f" s1 ⊇ s2: {set1.issuperset(set2)} (using set1.issuperset(set2))")
print(f" s1 ⊇ s2: {set1 >= set2} (using set1 >= set2)")

# Unique
print("Unique")
print(f" set1: {set1}")
print(f" set2: {set2}")

print(10*"-")
print("Permutations and Combinations")
from itertools import permutations, combinations
n = 3
k = 2
values = range(1, n+1)
print(f"n = {n} distinct values: {list(values)}")
P_nk = list(permutations(values, k))
print(f" {len(P_nk)} permutations of length k = {k}: P_nk = {P_nk}")

C_nk = list(combinations(values, 2))
print(f" {len(C_nk)} combinations of length k = {k}; C_nk = {C_nk}")

C_nk_set = set(C_nk)
P_nk_set = set(P_nk)

print(f" C_nk ∩ P_nk = {C_nk_set & P_nk_set}")