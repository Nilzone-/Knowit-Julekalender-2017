import numpy as np
size = 1000

def create_wall(x, y):
	return "{0:b}".format(x**3 + 12*x*y + 5*x*y**2).count("1") & 1

def build_grid():
	return np.array([create_wall(j+1, i+1) for i in range(size) for j in range(size)]).reshape(size, size)	

def visit(grid, x=0, y=0):
	if grid[x][y]: 
		return	
		
	grid[x][y] = 1
	
	if x > 0: visit(grid, x-1, y)
	if x < size-1: visit(grid, x+1, y)
	if y > 0: visit(grid, x, y-1)
	if y < size-1: visit(grid, x, y+1)


grid = build_grid()
print "Original grid\n"
print grid

visit(grid)

print "\n\nAfter search\n"
print grid

print "\n%d unvisited points in grid" % (size**2 - np.count_nonzero(grid))