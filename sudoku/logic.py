import os
import random

def cross(A, B):
    	"""Cross product of elements in A and elements in B."""
    	return [(a+b) for a in A for b in B]

def insert(value,r,c):
	global grid
        grid[r][c] = value
        
def check_avail(r,c):
	"""checks whether the index is empty or not"""
	global grid
	if grid[r][c]==0: 
		return True
	else : 
		return False			


def check_validity(value,r,c):
	"returns True or false"
	global grid
	global peers
	key=str(r)+str(c)
	for i in peers[key]:
		int_i=int(i)
		row=int_i/10
		col=int_i%10
		if grid[row][col]==value:
			return False
	return True	
		

def create_grid_hard():
	"""creats the initial grid"""
	global grid
        grid = [[0 for i in range(10)]for j in range(10)]
	global table
        table.clear()
	global win_counter
	win_counter = 0

	choicev=[1,2,3,4,5,6,7,8,9]
	choicei=[0,1,2,3,4,5,6,7,8]
		
	#generating 1 to 9 and putting it in a random position
	for value in range(1,10):
		while True:	
			r,c=random.choice(choicei),random.choice(choicei)
			if check_avail(r,c):
				if check_validity(value,r,c):		
					grid[r][c] = value
        				key = 'i'+str(r)+str(c)
        				table[key] = value
        				win_counter += 1
					break

	#generating random value and putting it in a random position
	for i in range(9):
		while True:
			value=random.choice(choicev)
			r,c=random.choice(choicei),random.choice(choicei)
			if check_avail(r,c):
				if check_validity(value,r,c):		
					grid[r][c] = value
        				key = 'i'+str(r)+str(c)
        				table[key] = value
        				win_counter += 1
					break
	display(grid)


def create_grid_easy():
	"""creats the initial grid"""
	global grid
        grid = [[0 for i in range(10)]for j in range(10)]
	global table
        table.clear()
	global win_counter
	win_counter = 0

	choicev=[1,2,3,4,5,6,7,8,9]
	choicei=[0,1,2,3,4,5,6,7,8]
		
	#generating 1 to 9 and putting it in a random position
	for value in range(1,10):
		while True:	
			r,c=random.choice(choicei),random.choice(choicei)
			if check_avail(r,c):
				if check_validity(value,r,c):		
					grid[r][c] = value
        				key = 'i'+str(r)+str(c)
        				table[key] = value
        				win_counter += 1
					break

	#generating random value and putting it in a random position
	for i in range(18):
		while True:
			value=random.choice(choicev)
			r,c=random.choice(choicei),random.choice(choicei)
			if check_avail(r,c):
				if check_validity(value,r,c):		
					grid[r][c] = value
        				key = 'i'+str(r)+str(c)
        				table[key] = value
        				win_counter += 1
					break
	display(grid)
		
def display(grid):
	"""displays the grid"""
	os.system('cls' if os.name=='nt' else 'clear')
	print "\n\n"
	width = 2
	line ="------+-------+------"
	count1=0
	for r in range(9):
		print "\t",
		count=0
		for c in range(9):
			print grid[r][c],
			count+=1
			if count==3 and c!=8:
				print "|",
				count=0
		count1+=1
		print 
		if count1==3 and r!=8:
			print "\t",line	
			count1=0
	print "\n\n"
	
########## identifier,finding peers of a square #########
digits   = '012345678'
rows     = digits
cols     = digits
squares  = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] +
   	    [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('012','345','678') for cs in ('012','345','678')])
units = dict((s, [u for u in unitlist if s in u]) 
              for s in squares)
global peers
peers = dict((s, set(sum(units[s],[]))-set([s]))
              for s in squares )

##########  ########################
global grid
global table
table = {}
global win_counter
win_counter = 0


