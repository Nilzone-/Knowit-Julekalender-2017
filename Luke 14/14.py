n = [1, 2, 4]
[n.append(n[i-3] + n[i-2] + n[i-1]) for i in range(3, 30)]
print n[-1]