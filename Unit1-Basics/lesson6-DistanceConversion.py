

# Begin by asking the user to enter a distance in miles
miles = input("Enter a distance in miles: ")

# The input function always returns a string, so we have to type cast.
miles = int(miles)

# Now we can make the conversion. There are about 1.609km in one mile.
kilometers = miles * 1.609


# Finally we can display the output.
output = "{} miles is equal to {} kilometers".format(miles, kilometers)
print(output)

# ----------- Exercises Below -----------------

# 1. This program doesn't intorduce itself. Add line 1 to explain to the user
#    that the program will convert distnace from miles to kilometers.

# 2. If the user enters 2.7 miles, the program will act like he had entered
#    exactly 2 miles. Modify the program so that it will use the decimal part.

# 3. It would be nice to round to only a few decimal places. Add line 11 to use
#    the built-in round function. it works like this.
#    roundedNumber = round(originalNumber, numberOfDigits)

