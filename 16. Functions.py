# Function is defined by using def

def newFunction():
    print("This is a new function")

#To call a function we just use nameoffunc()

newFunction() #calling a function

#We can also give arguments in a function inside ()
#We can give more arguments just seperate them by a comma

def myfunc(name, age):
    print("Your name is : "+ name)
    print("Your age is : "+ str(age))

myfunc("Kushal", 21) #calling a function with arguments


#IF number of arguments is not defined 

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


#return works same 

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))




