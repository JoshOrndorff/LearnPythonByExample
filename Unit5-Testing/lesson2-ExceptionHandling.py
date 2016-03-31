# So far, our functions have assumed that they received good arguments. But what
# if the caller passes a string when the function expected an int. In general
# the function will crash. The best thing we ca ndo here is raise an exception
# so the caller knows what went wrong.

def is_square(testNumber):
  '''
  This Boolean function takes a non-negative number (int or float) as an
  argument and returns True iff the number is a perfect square.
  '''
  
  # Before we begin calculating, let's make sure the argument is okay
  if type(testNumber) != int and type(testNumber) != float:
    # If the argument is not an int or float, we raise an exception.
    # TypeError is used whenever the problem is with the data type.
    raise TypeError("is_square must take an int or float.")
  
  # Try all integers from zero to see if they are the square root.
  possibleRoot = 0
  while possibleRoot ** 2 <= testNumber:
    # If the root squared gives the testNumber exactly, then it is a square.
    if possibleRoot ** 2 == testNumber:
      return True
            
    # Try the next possible Root
    possibleRoot += 1
  
  # We made it through the loop without returning, so testNumber isn't square.
  return False
  
  
# ---------------- Test Cases -----------------

# Case 1. Test a number that actually is square
print("The number 25 is square: " + str(is_square(25)))

# Case 2. Test a number that is not square
print("The number 22 is square: " + str(is_square(22)))

# Case 3. Test zero (the edge case)
print("The number 0 is square: " + str(is_square(0)))

# Now that we implemented the feature of raising an error when a non-number is
# passed in, we should make a test for that feature. These tests are tricky and
# must use try, except.
# Case 4. Test a string (not a valid data type)
try:
  is_square("some text")
except:
  print("A string caused the correct excecption.")
else:
  print("A string did not cause the correct exception.")


# ---------------- Exercises -----------------
# 1. This function should not take negative arguments. Test whether the argument
#    is negative, and if it is, raise an ValueError

# 2. Write a test for this new case.
