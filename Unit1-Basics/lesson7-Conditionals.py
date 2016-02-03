# We'll start by asking the users age. Remember age is a number.
age = input("How old are you? ")
age = int(age)

# Now we'll display a sentence based on how old they are. Note the syntax of the
# if statement. It is the word if, followed by some test, followed by a colon.
if age < 10:
  # Any lines that are indented like this will only execute if age < 10.
  print("That's pretty young.")
  print("It's only one digit.")
  
# To test for another case, we can use the word "elif". (Short for "else if")
# The elif test will only be used if the first test was not true.
elif age < 16:
  print("You aren't old enough to drive")

# We can have as many elif tests as we like, but they all have to match the
# indentation level of the original if.
elif age < 18:
  print("You are probably still in high school.")
  
elif age < 22:
  print("You're probably out of high school, but maybe still in college.")




  
# Finally we can have an else. The statements indented inside of else will run
# only if all of the otehr if and elif test have been false.
else:
  print("You're old")



# Finally, if they are exactly the same age as me, I'll tell them.
# This is a new if (not an elif or else) so it will be tested no matter what the
# previous test results were.
if age == 28:
  print("That's the same age as me.")
  
# ----------- Exercises Below -----------------

# 1. Change the age in the final test to match your own age.

# 2. Add another case on lines 25 - 27 to test whether the user is younger than
#    30. Include two lines of code in this case. One to print, "You're not quite
#    over the hill yet", and a second to print, "You're only 26" or however old
#    the user is.

# 3. Add an else to my final if clause to print, "We're not the same age, I'm
#    28".

# 4. In the else clause that goes with the first if (lines 27 - 28), the user
#    may feel sad that we call her old. Let's make her feel better by printing
#    on the next line, "Age is just a number."

# 5. Modify line 27 to use a format string like we learned in lesson 5.

