from collections import Counter

with open("anagramlist.txt") as f:
	print sum(w != w[::-1] and sum(1 for v in Counter(w).values() if v&1) < 2 for w in f.read().splitlines())
