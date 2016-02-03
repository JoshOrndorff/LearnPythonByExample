# The printing of our variables in the last few lessons has not been very
# convenient. Let's learn how to print variables of any type inline.

# First I'll set up some variables that we'll use throughout the program.
name = "Orndorff"           # string
luckyNumber = 5             #
height = 175.9              
favoriteAnimal = "platypus" 

# We learned in lesson one how to concatenate strings for printing.
output = "My name is " + name
print(output)

# But it isn't possible to combine a string with an int the same way.
# Uncomment to following lines to see the problem.
#output = "My lucky number is " + luckynumber
#print(output)

# One solution is to manually cast the number to a string like this.
output = "My lucky number is " + str(luckyNumber)
print(output)

# A better way is to use a format string.
output = "My lucky number is {}.".format(luckyNumber)
print(output)

# The syntax is specific, so note a few things:
#  - The curly braces {} go inside the string and act as blanks to fill.
#  - The .format() method goes immediately after the string.
#  - The .format() method takes one argument for each {} in the string.


# Here is a more complex example. Note that the formatting can happen separately
# from setting up the format string.
output = "My name is {}. I am {}cm tall, and I like the {}."
output = output.format(name, height, favoriteAnimal)
print(output)



# ----------- Exercises Below -----------------

# 1. On line 5 I've indicated that the type of name is a string by making a
#    comment. Do likewise for lines 6 - 8.

# 2. The formatting and printing can all be done on one line. Although this
#    isn't always the best choice, in simple cases, it is nice to be concise.
#    Add line 39 to make the program print "Orndorff's lucky number is 5."
#    Be sure to use a format string.

