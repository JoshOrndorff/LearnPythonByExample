
# Just give the user some basic instructions. For the rest of this unit,
# simple lines like this will not be commented as thoroughly.
print("I'll ask you for a bunch of text. Type \"done\" when you are finished.")

# Create an empty string. Although the string is empty right now, we will add
# to it as we go through the program.
combinedText = ""

# Another string that will eventually represent the user's input to the
# program. Although this string does have some content (and I really do love 
# platypi) the content is never shown to the user. We only need this string to
# not be empty so that we enter the loop on line 16.
userInput = "I like platypi."

# Here we use our first while loop. While is kind of like if because it tests
# the boolean expression, and enters the body of the loop if the expression is
# True. Unlike if, the while loop will continue to run over and over until the
# boolean condition becomes False.
while userInput != "done":

  # Take some actual user input. Notice that this overwrites the previous
  # contents of the userInput variable.
  userInput = input("Enter some text then press enter. ")
  
  # We'll add the input that the user just provided to the combinedText
  # variable. Remember the + operator can be ussed to concatenate strings as
  # as for actual math addition.
  combinedText = combinedText + userInput
  


# ---------------- Exercises -----------------
# 1. Change the initial value of the string on line 10.
#    Predict what will be different on the lines below. (Don't forget to comment
#    them so they don't affect your program.)

# 2. Change the initial value of the string on line 4.
#    Predict what will be different on the lines below. (Don't forget to comment
#    them so they don't affect your program.)

# 3. The program currently uses the phrase "done" to indicate that the user is
#    finished entering text. But if the user actually wants to enter the word
#    "done" there is no way to do it. Modify line 20 so that entering a blank
#    line will end the loop instead of the word "done".

# 4. Change line 25 to:
#    combinedText += userInput
#    This += operator is a shorthand for the full expression that we previously
#    used. The shorthand can also be used in math. In fact, +=, -=, /=, *= are
#    all valid math operators.
