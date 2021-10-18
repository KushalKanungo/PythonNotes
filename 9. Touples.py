# Tuple is written in ()
# Tuple are ordered and unchangable(we cannot remove, add, change items in tuple)
# Allow duplicate items


thistuple = (1, 2, 3, 4, 5)
print(thistuple)

print(len(thistuple))  # returns length of a tuple

tuple_with_different_datatypes = (
    "Hello", 1, 2, 2.5, True)  # can have different datatypes


# Access the tupple

print(thistuple[2])  # print 3rd value

print(thistuple[:4])  # print starting 4 items Negative indexing also works


# Updating tuples
# We cannot directly add items to tuple but their is a hack

y = list(thistuple)  # Create new list with items of tuple
y.append("New Item")  # appending in list / For removing we will use .remove()
thistuple = tuple(y)  # converting y to tuple and assigning to thistuple

# We can add a tuple to other

fruits = ("apple", "banana", "cherry", "papaya", "grapes", "guava")

thistuple += fruits  # adding tuple to fruits and assign to itself

# del thistuple
# it will delete our tuple


# Unpacking a tuple

# assign the value *items4 will be a list with remaining items
(item1, item2, item3, *item4) = fruits

print(item1+"  "+item2+"  "+item3)
print(item4)  # item4 is a lsit with remaing items


# Loops in tuple (iterating them)

for x in fruits:  # iterating full
    print(x)

for x in range(3):  # iterating to a certain index
    print(fruits[x])

i = 0
while i < len(fruits):  # using while loop
    print(fruits[i])
    i = i + 1


# join tuples

newtuple = fruits+thistuple  # we can add two tuples

newtuple = fruits*3  # fruits items 3 times

print(newtuple.index("banana")) #returns the index of banana exception if not found
