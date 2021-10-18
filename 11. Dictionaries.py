# Dictionaries are ordered changeable and does not allow duplicates
# Dictionaries are used to store data values in key:value pairs.

thisdict = {  # two items cannot have same key
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# .len() used to get length of a dictionaries
# .type() used to get type

# Accessing dictionaries

print(thisdict["model"])  # returns Mustang
print(thisdict.get("model"))  # returns Mustang using .get() Method

print(thisdict.keys())  # return a list of all the keys in the dictionary

# Add a new item to the original dictionary, and see that the keys list gets updated as well:
# .keys()

x = thisdict.keys()
print(x)
thisdict["Color"] = "Black"
print(x)  # X also Updated

# The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.
x = thisdict.values()
print(x)
thisdict["year"] = 2020
print(x)  # x also updated

# The items() method will return each item in a dictionary, as tuples in a list.
x = thisdict.items()
print(x)

# Check if key exist
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")


# Changing items

thisdict["brand"] = "Tata"  # Changed the brand to bata

# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.

thisdict.update({"year": 2060})  # updated year


# Adding Items
thisdict["Owner"] = "Kushal"

# remove Items
thisdict.pop("brand")  # remove brand
print(thisdict)

# Removing last added item
thisdict.popitem()  # Removed Owner
print(thisdict)

del thisdict["model"]  # Delete Brand

thisdict.clear()  # Empties whole dictionary


# Loops in dictionaries iterating

for x in thisdict:
    print(thisdict[x])  # Print all keys one bye one

for x in thisdict:
    print(thisdict[x])  # Print all values one bye one

for x in thisdict.values():  # print all values
    print(x)

for x in thisdict.keys():  # Print all keys
    print(x)

for x, y in thisdict.items():  # Print Both Items and Keys
    print(x, y)


#Coping a Dictionary

copieddict=thisdict.copy()
#or
copieddict=dict(thisdict) 