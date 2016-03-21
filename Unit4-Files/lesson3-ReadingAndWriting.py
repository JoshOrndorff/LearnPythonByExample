import os

# Since the file name will be used in several places, it is nice to make it a
# variable. That way if we later decide to change the file name, we only have to
# change it in one place instead of several. This makes the code "future proof".
filename = "userData.txt"

# Test whether the data file exists
if os.path.isfile(filename):
  
  # If the file does exist, we should read the data from it and print that data
  # for the user to see.
  
  # Open the file in read mode.
  f = open(filename, 'r')
  
  # Read the contents of the file into a single string
  oldContent = f.read()
  
  # Display the text from last time to the user
  print("Last time you ran this program you entered:\n{}".format(oldContent))
  
  # Since we're done reading from the file, we should close it.
  f.close()
  
else:
    
    # If the file does not exist, then the user hasn't run the program before
    # (or they manually deleted the data file.)
    print("You haven't run this program before.")
    
# Blank line
print()

# Get some new content from the user. This is just a regular old string.
newContent = input("Enter some text to store for later: ")

# Now we want to write the user's text to the file so it is saved for later. In
# order to do that we'll open the file in 'w' mode. This will replace the
# existing file with a blank file, or create a new file if there isn't one.
f = open(filename, 'w')

# Now that the file is open we can write the user's string into it.
f.write(newContent)

# Don't forget to close the file
f.close()

# And we can tell the user that we've saved their info in a safe place.
print("Thanks! I've saved that text  for next time. (Run the program again.)\n")
  
# ---------------- Exercises -----------------
# 1. The program REQUIRES the user to enter text every time. What if they just
#    want to see what they typed before without changing it. Modify the program
#    so that if the user enters a blank line, the file is not changed.
