# Sets are used to save multiple items
# They are unordered and unindexed
# Sets are unchangable
# Duplicates items not allowed unlike lists and tuples
# Written in {}
# Can containe different data types in one set

thisset = {"apple", "banana", 1, True, "cherry"}

# It will not work as it is unindexed
# print(thisset[0])

# loop through set
for x in thisset:
    print(x)

# Add Items

thisset.add("New Item")
print(thisset)

# Remove items
thisset.remove("New Item")  # Will rase error if item not dound

# will not raise an error so we prefer it over remove()
thisset.discard("New Item")

# Remove the last Item
thisset.pop()  # cannot give index no.


# To add two sets we use .update()
dummyset = {"hellow", 3, "Items"}

thisset.update(dummyset)  # added dummyset to thisset

# We can also add lists tuples in sets

thislist = ["new", "list", "added"]
thisset.update(thislist)  # added list to set

# Join two sets
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 0}
set3 = set1.union(set2)

# .update()

set2.update(set1)  # add items of set1 to set2
print(set2)

# Both union() and update() will exclude any duplicate items.

# Keep only duplicates

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

# It updates x  similartly .symmetric_difference_update()
x.intersection_update(y)

print(x)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)  # returns the new set similarly .symmetric_difference()

 

