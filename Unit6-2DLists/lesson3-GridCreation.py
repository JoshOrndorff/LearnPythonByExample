import random

# Often, you want to build up a grid inside of your code. This lesson covers
# that process by making a grid compatible with our Where's Waldo program from
# last time.

# We'll need some non-waldo people to populate most of the grid.
nonWaldos = ["Marge", "Homer", "Bart", "Lisa", "Maggie"]

# Start with an empty grid and later add rows to it. We're actually going to
# fill EVERY posistion with a non-Waldo, then go back and replace one of them
# with Waldo.
grid = []

# To make a 4X4 grid, make a new row and append it to the grid 4 times.
for r in range(4):
	
	# Just like the grid itself, the new row starts empty an get's built up.
	newRow = []
	for c in range(4):
		# random.choice chooses a random item some list. In this case is just
		# chooses one of our non-waldos
		newRow.append(random.choice(nonWaldos))
		
	# Once the row is made, don't forget to actually put it in the grid.
	grid.append(newRow)


# Now we just have to stick waldo in there somewhere.
waldoRow = 1
waldoCol = 2
grid[waldoRow][waldoCol] = "Waldo"


# Print the grid to see whether we were successful. The printing doesn't look
# very good yet. I'll leave that to you.
print(grid)


# ---------------- Exercises -----------------
# 1. Waldo is pretty easy to find since he is at (1, 2) every single time. Use
#    the random module's funstions to put Waldo at a different location. For
#    extra street cred, try to do this using only random.random()

# 2. Change the grid's dimensions to be 5X5.

# 3. Change the grid's dimensions to be 3X5.

# 4. ADVANCED: Convert this program to use a function that takes in dimensions
#    as arguments, and returns the created grid.
