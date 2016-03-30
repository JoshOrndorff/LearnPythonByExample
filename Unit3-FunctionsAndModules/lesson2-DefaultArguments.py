# We'll define a function just like before. This function takes three arguments.
# But notice that I've set two of the arguments  equal to specific values right
# here in the definition line. That means these arguments have default values.
# It doesn't mean that startingNumber will always equal 1. It means that if the
# client doesn't supply a starting number, it will default to one.

def print_list(dataList, startingNumber = 1, allCaps = False):
  '''
  Print to contents of the list, dataList, directly to the screen, in a
  human-friendly numbered format. Nothing is returned.
  
  Optional arguments:
    startingNumber: the first item nuber, defaults to 1
    allCaps: whether strings should be transformed to all caps, defaults to False
  '''
  # Setup a counting variable to keep the number increasing throughout the list.
  counter = startingNumber
  
  # Loop through each item in the list.
  for item in dataList:
    # Create a string of the item with a number before it.
    line = "{}. {}".format(counter, item)
    
    #TODO Convert to caps.
    
    
    # Change the counter for next time through
    counter += 1
    
# ---------------- Main Program -----------------

# Make a simple list to test out our function.
sports = ['Cross Country', 'Swimming', 'Skating', 'Slacklining']

# Let's try out the most basic usage of the print_list function
print("Basic sports list:")
print_list(sports) # We have ONLY supplied the required argument.
print()

# Now let's try to make the numbering start at 5 instead of 1.
print("Start numbering at 5:")
print_list(sports, 5)
print()

# Now let's try to print the list in caps, and make the numbering start at 7.
# (NOTE: The caps feature won't work until you write it -- see exercise ??)
print("All caps, start numbering at 7.")
print_list(sports, 7, True)

# What if we want to use the all caps feature, but use the default numbering?
# We can't just do print_list(sports, True) because python will think True is
# the second argument, startingNumber. But really it is the third argument. In
# such a case we have  to refer to the arguments by name.
print("All caps, default numbering.")
print_list(sports, allCaps=True)
print()






# ---------------- Exercises -----------------
# 1. The all caps feature is actually not yet implemented. Add line 25 to make
#    that feature work. Remember to remove the TODO from line 24 when you've
#    done it.

# 2. Call the function again in such a way that it prints the sports starting
#    with number 3 and does not use all caps.

# 3. Add another optional argument called stepSize to the function definition.
#    The stepSize arugment allows the lsit to be printed with non-consecutive
#    numbers. For example:
#    2. Cross Country
#    4. Swimming
#    6. Skating
#    8. Slacklining
#
#    You can decide what a good default value for stepSize is.





