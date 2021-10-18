# Lists are used to store multiple items in a single variable.

mylist = ["apple", "orange", "banana", "grapes", "guava"]
print(mylist)

# Some Points to remember
# 1. Lists items can be same
# 2. Ordered and Changeable
# 3. Can contain different data types

print(len(mylist))  # print length of mylist

mylist[0]  # return first item from list
mylist[2:4]  # returns item from 2 to 4 in list datatype

# Check list (in /not in)
if "apple" in mylist:
    print("Yes, 'apple' is in the fruits list")
    print("Yes, 'apple' is in the fruits list")

# Change items in list it will replace the item

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# The length of the list will change when the number of items inserted does not match the number of items replaced.
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# To insert a new list item, without replacing any of the existing values, we can use the insert() method.
thislist.insert(2, "watermelon")
print(thislist)

# Add item at end append()
thislist.append("addedAtEnd")

# add items from one list to another
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).


# To remove an item use list.remove("Name")
thislist.remove("apple")

thislist.pop(2)  # remove 2nd index item
thislist.pop()  # removes last item if not specified
del thislist[0]  # remove 0 index item
del thislist  # removes entire list




thislist = ["apple", "banana", "cherry"]
thislist.clear()  # it will clear the list it will not remove the list entirely

for x in thislist:  # iterate list same as a string
    print(x)

thislist = ["apple", "banana", "cherry"]  # iterate for 2 times
for i in range(2):
    print(thislist[i])  # return apple and banana only

# A short hand for loop that will print all items in a list:
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# above code can be written as
newlist = [x for x in fruits if "a" in x]

# Syntax 
# newlist = [expression for item in iterable if condition == True]

fruits.reverse() #reverse the items in list
fruits.sort() #sort alphabatically or numerically
otherfruits=fruits.copy() #copy the items in fruits to otherfruits
newfruits=list(fruits) #another way to copy 


addedlists=fruits+newlist #addes to listsz

numbers=[1,2,3,4,5,4,3,6,32,65,24,1,4,3,2,5,3,5,76]
x=numbers.count(5)  #returns the number 5 appears in the list





