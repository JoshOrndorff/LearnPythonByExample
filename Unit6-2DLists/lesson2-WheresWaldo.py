# Let's  make a 2D list that contains a bunch of people. Since all these strings
# are different lengths it would be easy for this table to look messy. Using
# white space effectively can help the data look more organized.
people = [["Jack",   "Abagail", "Waleed"  ],
          ["Rebeca", "Obi",     "Orndorff"],
          ["Simon",  "Waldo",   "Jamie"   ]]



# Our goal is to figure out where in the grid the name "Waldo" appears, and
# print its coordinates. Algorithm-wise that means looking through each row,
# and within each row looking through each name until we see Waldo.
rowCounter = 0
for row in people:
	
	
	colCounter = 0
	for item in row:
		
		if item == "Waldo":
			print("Found him at location {}, {}".format(rowCounter, colCounter))
		
		colCounter += 1
	rowCounter += 1


# ---------------- Exercises -----------------
# 1. Change the search so that it will find "waldo", "WALDO", and "walDO" as
#    Well as just "waldo".

# 2. Change the for loops to while loops. What looping condition should we use
#    to make sure we don't miss any rows or items in those rows?

# 3. Modify lines 6 and 7 to add a fourth row of people to the list. Does your
#    code still find waldo correctly? What if Waldo is in the bottom row?

# 5. What happens if waldo appears more tha once in this grid?

# 4. ADVANCED: Convert this program to use a function called wheres_waldo that
#    takes a grid as an argument, and returns the coordinates. What happens
#    if Waldo appears more than once in this grid? What happens if Waldo isn't
#    in the grid at all?
#
#    Hint: your return line line should look something like:
#
#    return rowCounter, colCounter
#
#    That line returns a tuple which we haven't formally seen... yet.
