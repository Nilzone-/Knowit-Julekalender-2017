def is_juletall(nn):
	is_valid = False	
	k = nn
	
	while True:
		tmp = sum(int(n)**2 for n in str(nn))
		if tmp == 1:
			is_valid = True
			break
		if tmp == 4:
			break
		nn = tmp				
	return is_valid


size = 10000000
s = 0
for i in range(1, size+1):
	s += i if is_juletall(i) else 0
    
	if(i % 100000 == 0):
    		print "progress: {}%".format(100*i/size)

print s