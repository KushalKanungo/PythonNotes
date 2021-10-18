# String as a array

# from typing import Text


a = "Hello, World!"
print(a[1])

# Looping through String
for x in "Orange":
    print(x)

# String Length
print(len(a))

# Check String (in / not in )
txt = "The best things in life are free!"
print("free" in txt)  # returns boolean

if "free" in txt:
    print("Yes free is present")

if "Hello" not in txt:
    print("No, Hello is not present")


b = "Hello, World!"
print(b[2:5])  # It will print from value 2 to 5

print(b[:6])  # Slice from start

b[3:]  # slice from end

b.upper()  # lower case

b.lower()  # uppercase

b.strip  # remove white space

b.replace("H", "J")  # Replace String

print(print(a.split(",")))  # returns ['Hello', ' World!']

