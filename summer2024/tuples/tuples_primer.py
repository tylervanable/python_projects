"""
    Discuss and give examples of tuples.

    Tyler
    5/25/24
"""

# Discuss tuples.
print("Tuples are similar to lists, like a collection of values,")
print("Like lists, tuples have a particular order.")
print("However unlike lists, tuples are immutuable, meaning they CANNOT be changed.")
print("This means that once a value is assigned to an index position, we cannot")
print("reassign to another a value like in a list.")
print("Once an element is inside a tuple, it cannot be reassigned.")
print("e.g. coords = (item1, item2)")

# Create a tuple of coordinates of New York City.
coords = ("NYC", 40.71, 74.00)

# Insert a line break.
print()

# Discuss and demonstrate similarities in working with tuples.
print("In the example above, we mixed object types, such as a string and floats.")
print("In general tuples have fewer available methods, and less flexibility.")
print("We can find how many elements are in a tuple with the len() function...")
print(len(coords))
print("We can also slice and index a tuple. Demonstrating slicing..")
print(coords[0])
print(coords[-1])
print("Demonstrating counting a tuple...")
print(coords.count("NYC"))
print("Demonstrating indexing...")
print(coords.index("NYC"))
print("Notice: that the .index() method ONLY returns the index for the")
print("first instance of what is within the argument.")

# Insert a line break.
print()

# Demonstrate immutability with tuples. 
print("If we try to reeassig the first index, 'NYC', to its full name...")
print("using 'coords[0] = \"New York City\"', we get a TypeError.")
print("TypeError: 'tuple' object does not support item assignment")

# Discuss the benefit of using tuples over lists.
print("We use tuples for data integrity, when we do not want to reassign a")
print("value to a new value.")
print("We also use tuples when we do not want elements' order to get flipped.")
