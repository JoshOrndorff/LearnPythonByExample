# Programs oftem have to perform identical or similar tasks over and over again.
# For example, we have printed text to the screen dozens of times already. To do
# it we used the print function. There are lot's of other useful function like
# len(), abs(), chr(), ord(), and thousands more. But sometimes, the function
# need doesn't exist. In that case you have to write it yourself.


# We define functions using the keyword def.
# Then we give them a name. In this case the name is double_number.
# In parentehses we list the arguments (aka parameters) the function needs.
def double_number(originalNumber):
  """
  This function takes in one argument called original number. The argument can
  be any number (int or float), positive or negative. The function will double
  that number and give the answer back to the client.

  PS. This text is known as a documentation string or "docstring". All functions
  should have one, although they don't have to be as verbose as this one. Just
  write enough that other programmers (including your future self) will know
  what this function was supposed to do.
  """

  # Calculate the doubled number
  doubled = originalNumber * 2

  # The return statement gives the answer back to whoever called the function.
  return doubled


def tripple_number():
  """

  """
  #TODO Complete this function



# ---------------- Main Program -----------------

# Even though the function was written above, it won't actually execute until we
# call it. Let's try it a few times.

# Notice here that I passed in a variable called x. When the function runs, the
# value of x gets copied to originalNumber. If you like vocab, originalNumber is
# called the "formal parameter" and x is called the "actual parameter".
x = 4
doubleX = double_number(x)
print("Doubling 4 gives {}".format(doubleX))

# We don't have to name the formal parameter
double3 = double_number(3)
print("Doubling 3 gives {}".format(double3))

# We don't have to name the answer either. Here we put the entire function call
# in the format string. Think of the return value simply replacing the function
# call. In this case the answer, 10, replaces double_number(x).
x = 5
print("Doubling 5 gives {}".format(double_number(5)))

# The program crashes if I pass the wrong number of parameters.
#TODO Fix these calls so the program doesn't crash.
print(double_number())
print(double_number(4, 5))

# The program does NOT crash if I omit the argument list entirely. This behavior
# seems weird, but it allows some very powerful "higher-order" techniques that
# we'll learn later. For now you'll always want to include the argument list.
#TODO Fix this call so the program actually doubles something.
print(double_number)

#TODO Call your tripple number function here




# ---------------- Exercises -----------------
# 1. Fix the calls on lines 62 and 63 so that they double the numbers 4 and 5
#    respectively. Remember to remove the TODO when you are finished.

# 2. Fix line 69 so the program actually doubles something. By now you know to
#    remove the TODOs as you complete them, so I'll stop reminding you.

# 3. Complete the tripple_number function that begins on line 30. Remember to
#    include a formal parameter and a docstring. When you have the function
#    written, call it near line 72 to make sure it works

# 4. On lines 51-52 we learned that parameters don't have to be named (although
#    they certainly may). On lines 57-58 we learned that results don't have to
#    be named (although they too may be). Modify your call to tripple_number on
#    line 72 so that it combines both of these techniques. The result should be
#    a one-liner.
