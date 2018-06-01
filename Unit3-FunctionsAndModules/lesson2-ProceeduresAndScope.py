
def say_some_names():
  """
  This function Prints out the names of the user and the author. It doesn't
  take any arguments.

  It also doesn't have any explicit return value, so it returns None.

  ps. Functions that print to the screen rather than returning a value are
  sometimes called "proceedures".
  """

  # This variable has the same name as a variable that's in the main program.
  # This one has "local scope" which means it only exists inside the function.
  # Because they have the same name, there is no way to access the "global
  # scope" version from the main program. So the local one "shadows" the global.
  authorName = "Stoofey"
  print("The author's name is {}".format(authorName))

  # There is no local copy of userName, so the global one is still accessible here.
  print("The user's name is {}".format(userName))



def count_to_five():
  """
  This function prints the numbers 1 through 5 to the screen.
  It also returns the value 5 when it is done.
  """

  # Reminder the range function goes up to but not including 6
  for i in range(6):
    print(i)

  return 5

# ---------------- Main Program -----------------

authorName = "Joshy"
userName = input("What is your name? ")
print()

# Report both of our names.
print("The author's name is {}".format(authorName))
print("The user's name is {}".format(userName))
print()

# Now have the function, say_some_names, report our names.
# Even when the function doesn't take any arguments, you still need to have the
# parentheses to CALL the function.
say_some_names()
print()

# Let the function count to five. Can you figure out why it prints 5 twice?
print(count_to_five())
print()



# ---------------- Exercises -----------------
# 1. I claimed that removing the parentheses from line 51 would change the not
#    actually call the function. Remove them and see what happens. Put them
#    back afterward if you like.

# 2. Did you figure out why 5 prints twice? Remove the return on line 35. (If
#    you want extra street-cred, update the docstring to say "proceedure"
#    instead of function.) Now run the program again and see what happens.

# 3. When there is no return value, the function always returns None. Confirm
#    this by temporarily wrapping the call on line 51 in a print.

# 4. Generally we don't want to print that None, so go ahead and remove the
#    prints from lines 51 and 55 (but keep the proceedure calls).

# 5. The count_to_five proceedure isn't very general. It just does the exact
#    same thing every time. It would be better if it could count to an
#    arbitrary number. Make it take an argument called n. And make the
#    proceedure count up to n instead of 5. Be sure to change the proceedure's
#    name and update it's docstring accordingly. Finally, call it a second time
#    on line 54 to show that it really can count to two different number.
