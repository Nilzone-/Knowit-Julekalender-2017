a = "".join(map(chr, range(65, 91)))
word = "OTUJNMQTYOQOVVNEOXQVAOXJEYA"

def encrypt(l):
	return ((a.find(l) * 2 + ord(l) + 1) % 26)

def create_lookup():
	return dict(zip(map(lambda x: a[encrypt(x)], a), a))
	
d = create_lookup()
#print d
print "".join([d[w] for w in word])