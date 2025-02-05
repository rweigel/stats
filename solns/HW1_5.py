S = set(range(1, 101))
V = set(range(1, 51))
M = set(range(26, 66))
X = set(range(67, 101))

notV = S - V
notM = S - M

print(f"1. {len(V.union(M))/100} = Prob. selected student has at least one of the two types of cards")
print(f"2. {len(notV & notM)/100} = Prob. selected student has neither card type")
print(f"3. {len(V & notM)/100} = Prob. selected student has a Visa but not MasterCard")
