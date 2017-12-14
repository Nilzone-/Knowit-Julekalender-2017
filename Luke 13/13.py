from itertools import compress

with open("loot.txt", "r") as f:
	p = sorted([int(line.split(",")[1].strip()) for line in f.readlines()], reverse=True)
	th = [bin(n).count('1') % 2 for n in range(len(p))]
	print sum(compress(p, th))