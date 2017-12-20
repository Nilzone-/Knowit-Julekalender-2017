with open("prisoners.txt", "r") as f:
	p = [int(l.strip())-1 for l in f]
 
done = [False] * 100
switch = False
count = 0

for i, visitor in enumerate(p):
	if visitor == 0:
		if count == 99:
			print i+1
			break
		switch = False
	elif not switch and not done[visitor]:
		count += 1
		switch = done[visitor] = True
