# Define a function. If functions are not yet familiar, please review the unit
# on fcuntions. I will not heavily comment the function here.

def is_square(testNumber):
  '''
  This Boolean function takes a positive number (int or float) as an argument
  and returns True iff the number is a perfect square.
  '''
  
  # Try all integers from one to see if they are the square root.
  # We want to stop looking when squaring the possible root gives a number
  # larger than the original test value.
  possibleRoot = 0
  while possibleRoot ** 2 <= testNumber:
    # If the root squared gives the testNumber exactly, then it is a square.
    if possibleRoot ** 2 == testNumber:
      return True
      
  # Try the next possible Root
  possibleRoot += 1
      
  # We made it through the loop without returning, so testNumber isn't square.
  
  
  
# ---------------- Test Cases -----------------

# Down here in the main program, we will not ask the user for any input.
# Instead, we will hard code several "test cases" that show whether our function
# works properly.

# Case 1. Test a number that actually is square
print("The number 25 is square: " + str(is_square(25)))

#TODO Case 2. Test a number that is not square



# ---------------- Exercises -----------------
# 1. So far we've tried a square number, and our function says it is a square
#    number. The test passes! But we also need to test a non-square number.
#    On line 36 write a test case for a number that is not square. Remember to
#    remove the TODO when you have finished

# 2. Your new test case shows that the function returns None for non-square
#    numbers. This test fails. That's becuase I forgot to return false in the
#    function. Add a return statement on line 23 to fix this bug, and make sure
#    both tests pass now.

# 3. Change the function so it accepts zero as well as positive numbers. Zero
#    is considered square because 0 * 0 = 0. Be sure to update the docstring
#    to say that the function can accept zero.

# 4. Now that the function can handle zero, write a test case for 0. Zero is
#    known as an "edge case" because it is the very edge of the acceptable range
#    of input. It is very important to test your edge cases.
