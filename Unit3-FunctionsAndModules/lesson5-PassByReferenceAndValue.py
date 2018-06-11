def change_the_number(someNum):
  '''
  This function takes in a number, someNum, assigns it a new value of 4, and
  returns it.
  '''
  someNum = 4
  return someNum

def change_the_list(someList):
  '''
  This function takes in a list, someList, appends a new value of 4, and
  returns it.
  '''
  someList.append(4)
  return someList

def change_the_string(someString):
  '''


  '''





# ---------------- Main Program -----------------

# Create a number, and print it out so the user can see it.
myNum = 3
print("myNum is  {}".format(myNum))

# Now call change_the_num and observe the result. When ints get passed to
# functions, what actually happens is that a copy gets passed in. So the
# function doesn't actually change the original number. This behavior is called
# "pass-by-value"
newNum = change_the_number(myNum)
print("myNum is  {}".format(myNum))
print("newNum is {}".format(newNum))

print()

# Create a list, and print it.
myList = [3, True, "Banana"]
print("myList is  {}".format(myList))

# Now call change_the_list and observe the result. When lists get passed to
# functions, the actual list gets passed with no copying. So any changes that
# happen to the list in the function will persist after the function returns.
# This behavior is called "pass-by-reference"
newList = change_the_list(myList)
print("myList is  {}".format(myList))
print("newList is {}".format(newList))

print()

#TODO Make a string and see whether it is passed by reference or value









# TODO Use the change_the_list function again, but this time pass in an explicit
# copy so the original doesn't get changed.







# ---------------- Exercises -----------------
# 1. We've tried ints and lists. Try the same thing with strings to see whether
#    they are pass-by-value or pass-by-reference. Implement the function on
#    lines 17 - 23. Then call it similarly to how I have on lines 58 - 65.

# 2. Python has a operator called `is` that will tell us whether two variables
#    are actually the same object. On line 40 put the code:
#    print(myNum is newNum)
#    It should say false because they are not the same object.

#    Do likewise on line 54. This time it should say true because the lists are
#    the same object. It may seem weird that a single list can have two names,
#    but the same happens with people. My friends call me Joshy, but my
#    teammates usually call me Orndorff. Nevertheless, I am only one person.

# 3. Sometimes you want to pass a list or other pass-by-referencer type to a
#    function withou mutating the original. In this case you can use the syntax:
#    listCopy = myList.copy()
#    Try this starting on line 69. Then use the `is` operator to confirm that
#    they are not the same object.

#    Using copy only copies the list itself. It does not necessarily copy the
#    members of the list. You may want to read up on the difference between
#    copy and deepcopy, or at least keep it in the back of your mind that there
#    is a difference. https://stackoverflow.com/q/17246693/4184410
