def is_prime(n):
	return all(n % j for j in range(2, int(n**0.5) + 1)) and n > 1
	
mirp = []
[mirp.append(i) for i in range(1000) if is_prime(i) and is_prime(int(str(i)[::-1])) and i != int(str(i)[::-1])]
	
print mirp	
print len(mirp)
