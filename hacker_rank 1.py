from itertools import groupby
S = list(input("Enter the number: "))
groups = []
for k, g in groupby(S):
    groups.append(list(g))
for g in groups:
    print((len(g), int(g[0])),end=" ")


