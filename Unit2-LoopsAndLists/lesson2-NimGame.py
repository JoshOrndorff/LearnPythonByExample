
# Instructions
print("There is a pile of 20 marbles.")
print("You and the computer take turns removing 1, 2, or 3 marbles.")
print("You do not want to take the last marble.")

# The game starts with 20 marbles
marblesLeft = 20

# And it ends when there are zero marbles left. We will continue to loop through
# the process of taking marbles away until there are zero left.
while marblesLeft != 0:

  # The user goes first. Ask how many marbles they will take.
  print("There are {} marbles left".format(marblesLeft))
  userTakes = input("How many will you take? ")
  
  # We expect them to give us an integer, so we cast the string to an int.
  userTakes = int(userTakes)
  
  #TODO We don't want them to cheat, so make sure they take 1, 2, or 3 marbles.
  # Comments that start with #TODO are notes to the programmer, that we should
  # add a feature at some later time.
  
  
  
  
  
  # Now we'll actually subtract the marbles the user took from the pile.
  marblesLeft = marblesLeft - userTakes
  
  # Test whether the user took the last marble.
  if marblesLeft == 0:
    # If the user did take the last one, he loses.
    message = "Sorry you lose"
  else:
    # If he did not take the last one, the computer goes.
    # For simplicity, let's have the computer always take one marble.
    # This is not the best strategy for the computer, but that's okay.
    #TODO Make the computer play smarter.
    computerTakes = 1
    
    # Tell the user how many marbles the computer took.
    print("The computer takes {} marbles.\n".format(computerTakes))
    
    # And again, actually subtract the marbles the computer took.
    marblesLeft = marblesLeft - computerTakes
  
  # Test whether the computer took the last marble.
  if marblesLeft == 0:
    message = "Horray! You win!"
    
# Finally, after the loop ends, we tell the user the outcome of the game.
print(message)
    
  
  
# ---------------- Exercises -----------------
# 1. Remember last titme when we used the += operator? This program is a good
#    opportunity to practice those shorthand operators. Modify line 26 so it
#    uses the -= operator. Are there other places we could use that operator?

# 2. Let's update that #TODO to make sure the user takes 1, 2, or 3 marbles.
#    There may not be enough blank lines. Feel free to add more.

# 3. There is another #TODO. Can you make the computer play better strategy?

# 4. What if there is only 2 marbles left, and the user tries to take 3? Can
#    we make the program handle this situation? One solution is to consider the
#    user a cheater and make him lose. A more difficult solution is to tell him
#    there are not 3 marbles left and let him try again.
