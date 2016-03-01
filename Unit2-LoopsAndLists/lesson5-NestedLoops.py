# Create two empty lists. Both of which will be populated with numbers
numbers = []
otherNumbers = []


print("Tell three numbers.")
# Use the range function to loop three times.
# The looping variable i will iterate through the numbers 0, 1, 2
# But I'll never use them. It is okay to use a simple variable name like i
# when you are just looping through integers.
for i in range(3):
  number = int(input("> "))
  numbers.append(number)
  
# The same loop to get three more numbers for the second list.
print("Tell me three more numbers.")
for i in range(3):
  number = int(input("> "))
  otherNumbers.append(number)
  
  
  

# We'll check whether any of the numbers appear in both lists. Since we haven't
# started yet, we haven't foudn any matches yet. I'll make a variable to
# represent that.
matchFound = False

# I'll also make counters for each loop. You'll use these in the exercises.
outerLoopCounter = 0
innerLoopCounter = 0

# In order to do this we have to compare each number in the first list with each
# number in the second list. The word 'each' usually indicates that you'll want
# to use a for loop.
for number in numbers:

  # This outer loop will loop us through each item in the first loop.
  # For a given number in the first list, we will need to compare to each item
  # in the second list. So we need to loop through the second list as well.
  for otherNumber in otherNumbers:
  
    # Now that we have selected a number from each list, we just compare them.
    if number == otherNumber:
      matchFound = True




# Now that we have compared all the possibilities, we just have to tell the user
# whether there were any matches. Note that matchFound is a Boolean, so I don't
# neem to use a comparison operator (eg. don't have to use matchFound == True).
if matchFound:
  print("There was overlap between the lists.")
else:
  print("There was no overlap between the lists.")

# Here we'll show how many times each loop ran. These won't work until you
# complete exercise 1.
#print("The outer loop ran {} times.".format(outerLoopCounter))
#print("The inner loop ran {} times.".format(innerLoopCounter))


# ---------------- Exercises -----------------
# 1. I made counter variables to keep track of how many times each loop ran.
#    In order to make those counters work, increment the variables each time
#    through the corresponding loop. Then uncomment lines 60 and 61 to see the
#    results. Make predictions of what the results will be.

# 2. Right now the program just tells us whether there was any overlap, but does
#    not tell us which numbers overlap. Make a new list called overlap, on line
#    4 and add all of the overlapping numbers to it.
#    Then, at the end, tell us which numbers were in both lists.

# 3. This program has both lists the same length. Is that necessary? What if the
#    first list is longer? Change the code so that the first list has five
#    numbers. Predict whether it will still work, and how many times each loop
#    will run.

# 4. ADVANCED: This program uses only two lists. Modify the program to have
#    three lists, and discover whether any numbers were in all three.
#    Making this change will change the line numbers, so my references might not
#    make sense anymore.

# 5. ADVANCED: I use two different loops (on lines 11 and 17) to create the two
#    original lists. These could also be combined into one nested loop. Modify
#    these lines to use nested loops to take the input numbers.
