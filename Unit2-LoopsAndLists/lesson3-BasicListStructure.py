
# A list is a new data type kind of like string, int, bool, and float. The big
# difference between a list and these other types is that lists contain many
# pieces of data in it. To create a list, use square brackets, and separate
# each element in the list with commas.
animals = ["cat", "dog", "fish", "three-toed sloth"]

# We can print lists like any other data type. (Although it doesn't look pretty)
print("The animals are: ")
print(animals)
print()

# We can also print individual elements in a list by referencing their index.
print("The third animal is: ")
print(animlas[3])
print()

# But be careful because the indicies start at 0.
print("The zeroth animal is: " + animals[0])
print()

# If you enter too high of an index, you will get a pretty helpful error.
# Uncomment the following line to see the problem.
#print("The tenth animal is: " + animals[10])




# You can also access elements from the end of the list with negative numbers.
print("The last animal is: " + animals[-1])
print()

# Like strings, lists have a length and work with the len() function.
print("There are {} animals.".format(len(animals)))





# The append method allows us to add new items to a list.
newAnimal = input("Tell me a new animal: ")
animals.append(newAnimal)


# And we can show that the list is longer now.
print("Now the animals are: {}".format(animals))




# We can also remove items from a list with the remove method. Let's ditch cat.
animals.remove("cat")
print("I've removed the cat.")
print("Now the animals are: {}".format(animals))





# Finally, there is a nice method to sort a list. Strings get sorted
# alphebetically, ints and float from low to high. If you have a list that
# contains both strings and numbers, this simple sort will usually not help.
animals.sort()

# And we'll print the list one more time to see that it is sorted.
print("The sorted animals are:")
print(animals)

# ---------------- Exercises -----------------
# 1. On line 43. Add "dinosaur" to the list of animals, then on line 34
#    print the entire list of animals.

# 2. Modify line 43 so that it inserts dinosaur in the middle of the list
#    instead of at the end. You will need to use the insert method like this:
#    nameOfList.insert(indexToInsertBefore, "Thing to insert")

# 3. We saw how to remove "cat" from the list on line 52. But what happens when
#    "cat" appears in the list twice. Run the program again and when it asks you
#    to give a new animal, tell it "cat". Now what happens when we remove "cat"?
#    Can you think of any problems that might occur?

# 4. Modify the program so that it will remove all instances of "cat" instead of
#    just the first instance. You will probably need a loop.



