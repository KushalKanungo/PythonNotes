# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.

x = 5
y = "Kushal"
print(x)
print(y)

# Variables do not need to be declared with any particular type,
# and can even change type after they have been set.

a = 5
a = "5 changed to string"
print(a)


# Type Cast
x = str(3)  # 3 is stored as a string
y = int(3)  # stored as int
z = float(3)  # Stored as 3.0

# To get type of Variable
print(type(x))
print(type(y))

# Variable are case sensitive a and A are not equal

# We can assign multiple values in one go
no1, no2, no3 = "Apple", "Orange", "Banana"

# If you create a variable with the same name inside a function, this variable will be local,
# and can only be used inside the function. The global variable with the same name will remain
# as it was, global and with the original value.

x = "awesome"


def myfunc():  # def is used to create a function
    x = "fantastic"
    print("Python is " + x)


myfunc()
print("Python is " + x)

# global keyword can create a global variable even if it used in a function

global newvar
newvar = 9
print(newvar)
