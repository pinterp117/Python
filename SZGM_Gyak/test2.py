from itertools import permutations

seq = permutations(['a', 'b', 'c', 'd'])

for p in list(seq):
   print(p)