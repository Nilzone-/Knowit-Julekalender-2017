import numpy as np
size = 10

def create_grid():
	return np.zeros(size**2, dtype=np.uint8).reshape(size, size)
	
def nbrs(x, y):
	options = [(x+2, y+1), (x+2, y-1), (x-2, y+1), (x-2, y-1),
			   (x+1, y+2), (x+1, y-2), (x-1, y+2), (x-1, y-2)]
	return [(x, y) for (x, y) in options if 0 <= x < size and 0 <= y < size]
	
def xy(func, arr):
	return func(arr, key=lambda x: x[0]*10+x[1])

def move(grid, x=0, y=0, count=0):
	points = nbrs(x, y)		
	if count == 200: return

	arr = [point for point in points if grid[point] == grid[x,y]]
	grid[x,y] ^= 1
	x, y = xy(min, arr) if len(arr) > 0 else xy(max, points)
	
	move(grid, x, y, count+1)


grid = create_grid()
print "Before:\n"
print grid

move(grid)

print "\nAfter:\n"
print grid

print "\nNumber of black squares: %d" % np.count_nonzero(grid)