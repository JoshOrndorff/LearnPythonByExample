# Lists can contain any other data type such as numbers or strings.
numbers = [4, 7, 10, -5, 2]
words   = ["fish", "tree", "steel", "compiler"]


# Lists can also contain other lists. We can think of a list-of-lists as a two-
# dimensional list, or grid. Each inner list represents a row in the grid. We
# can even use spaces to line up each inner list in a grid-like way.
grid = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]


# All of the normal rules about indexing and slicing still apply.
print("The first numer is {}".format(numbers[0]))
print("The last two words are {}".format(words[-2:]))
print("The grids middle row is {}".format(grid[1]))
print()


# We can access individual items in the grid by first picking out their row
# Then choosing the correct item in that row. Let's pick out the item in
# row 2, column 1. (That's the 8; make sure you know why.)
secondRow = grid[2]
item = secondRow[1]
print("The item at position 2, 1 is {}".format(item))


# Since each row in the table is just a list, we can easily add new rows to
# by creating them as new lists and appending them to an existing table.
newRow = [10, 11, 12]
grid.append(newRow)


# Show the new fourth row in the grid.
#print("The new fourth row is.....


# Adding a column is also possible, but takes a little more work.







# ---------------- Exercises -----------------
# 1. To make sure we successfully added that new row, let's print it out.
#    Complete (and uncomment) line 36 to show the row was successfully added.

# 2. On lines 24 and 25 I accessed an item in two steps. This is probably the
#    clearest way to introduce the material, but in practice it's much more
#    common to do that in one step. Replace lines 24 and 25 with a one-liner
#    that performs the same task.

# 3. ADVANCED: Adding a row to the grid was relatively easy. Adding a column is
#    is also possible, but it means adding an item to each row that is already
#    in the grid. Starting around line 40, add a fourth column of all 0s to
#    the grid. When you're done the grid should look like this.

#    1  2  3  0
#    4  5  6  0
#    7  8  9  0
#    10 11 12 0
