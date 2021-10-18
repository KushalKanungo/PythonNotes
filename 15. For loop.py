# For loop in python is very different from other programming language.
# Here we use it to iterate in a list, tuple, dic, or set.
# More like a iterate method in other languages


fruits = ["apple", "banana", "cherry"]
for x in fruits:  # iterate in a list
    print(x)

for x in "banana":  # iterate in a string
    print(x)


# break and continue will work same

for x in range(6):  # loop upto 6 from 0 range() function
    print(x)

for x in range(2, 6):  # 2,3,4,5
    print(x)

for x in range(2, 30, 3):  # 3rd value is increment parameter
    print(x)  # 2,5,8,11,14,17,20,23,26,29


#Nested Loop

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


# we can also use pass statement here so we dont have to leave loop empty
