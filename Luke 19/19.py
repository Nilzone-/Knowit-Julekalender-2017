from numpy import array, savetxt
a = array([[" " for i in range(31)] for j in range(21)])

with open("path.txt", "r") as f:
	path = map(lambda x: [int(x[0]), x[1]], [l.strip().split(", ") for l in f.readlines()]) 
	
x, y = -1, 10
for n, d in path:
	if d == "north":   a[x-n:x+1, y] = "N"; x -= n
	elif d == "south": a[x:x+n+1, y] = "N"; x += n
	elif d == "east":  a[x, y:y+n+1] = "N"; y += n
	elif d == "west":  a[x, y-n:y+1] = "N"; y -= n

savetxt("answer.txt", a, fmt="%s")