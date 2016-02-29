# Make a list of ordinal words to demonstrate the use of a for loop.
ordinals = ['first', 'second', 'third', 'fourth', 'fifth']

# A for loop is used when you want to perform the same operations FOR each item
# in a list. (Technically it can be any iterable, not just a list.)
for currentWord in ordinals:
  # The for loop syntax is: for [someLoopingVarialbe] in [someList]:
  # The looping variable will be set equal to the first item in the list and the
  # loop code will run. Then the looping variable will be equal to the second
  # item and the code will run again. And so on until all list items are used.
  
  print("This is the " + currentWord + " time through the loop.")
print() # Just to get a blank line



# Make a new list to contain the user's favorite songs.
favoriteSongs = []

# In the past we've used a while loop to populate a list with user input.
# Now we'll populate the list using a for loop. Notice that this loop will run
# once for each ordinal in the list
for canBeCalledAnything in ordinals:
  song = input("What's your {} favorite song? ".format(canBeCalledAnything))
  favoriteSongs.append(song)
  
print()



# This is an ugly way to print a list:
print("Your favorite songs are :")
print(favoriteSongs)
print()



# A for loop is a perfect way to print the list more nicely.
print("Your favorite songs are :")
number = 1
for song in favoriteSongs:
  print("{}. {}".format(number, song))
  number += 1

print()



# ---------------- Exercises -----------------
# 1. The for loop in line 6 creates a looping variable called currentWord. That
#    name is fine, but it is very common to use the singular form of the list
#    name itself. Change the name of the looping variable to 'ordinal'. Don't
#    forget to change it in other places it is used too.

# 2. While you're at it, you could change the name of the looping variable in
#    line 20 as well. Do note that the variable really can be called anything.
#    But as always it is best to choose a meaningful name

# 3. The loop that asks users about their favorite songs works pretty well, but
#    it doesn't sound very natural to say 'your first favorite'. Put an if
#    statement in that loop to surpress the word 'first' from printing.

# 3. Add an ordinal to the list on line 2. Predict how the program will run
#    differently in comments in the lines below.
#
#
#
#
