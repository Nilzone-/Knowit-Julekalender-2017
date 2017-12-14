from itertools import count, takewhile	
size = 1000000
seq = [1, 2, 2, 3, 3]
n, nn = count(4), count(4)

[seq.extend([next(n)] * seq[next(nn)-1]) for _ in takewhile(lambda _: len(seq) < size, range(size))]
print(sum(seq[:size])) 