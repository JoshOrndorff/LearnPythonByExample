# So far we have learned about three types of data: string, int, and float.
# In some cases, we want to convert information from one type to another. The
# process of converting data from one type to another is called "type casting",
# or just "casting" for short.

# Let's make an int variable and print it.
luckyNumber = 5
print("My lucky number is:")
print(luckyNumber)
print()

# Now let's convert that variable to a float and print it again.
# Notice that it prints differently as a float even though the value is the same.
luckyNumber = float(luckyNumber)
print("My lucky number is:")
print(luckyNumber)
print()

# We may also want to convert a string to an int or float.
fingers = "10" # This is a string because of the quotes.
fingers = int(fingers)
print("How many fingers I have: ")
print(fingers)
print()

# But not all data can be converted successfully. Line 29 will produce an error
# if it is uncommented.
someText = "I like bananas"
#someText = int(someText)

# Some data can be converted successfully, but some information will be lost.
pi = 3.14159
pi = int(pi)

print("pi is: ")
print(pi)
print()


# ----------- Exercises Below -----------------

# 1. Modify line 21 to convert fingers to a string. To cast to string you will
#    need the str() function.

# 2. Uncomment line 29 to see its results. Why is there an error? What kind of
#    error does this line produce? Of course you will have to comment the line
#    again to continue when you are done.

# 3. On line 34, cast pi back to a float. What result do you expect?

