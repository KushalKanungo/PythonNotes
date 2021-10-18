# Arithmetic operators
1+1
1-1
1/1
1*1
# Some new operators

2**5  # 2*2*2*2*2
15//2  # returns 7(rounding off 7.5 to 7)

# Logical Operators
x = 15
x > 5 and x > 10  # returns true
x < 4 or x > 5  # returns true
not(x < 4 or x > 5)  # returns false (reverse the result)

# To compare objects (is /  is not)

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)  # returns True because z is the same object as x

# returns False because x is not the same object as y, even if they have the same content
print(x is y)

print(x == y)  # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


