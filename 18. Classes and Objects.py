# to create class in python we use 'class' keyword

class Myclass:
    x=5 #It is a class attribute
    y=10

obj=Myclass()  #To create object


obj.instan="It is a instance attribute"
obj.y=9 #Only change instance attribute(object attribute)

print(obj.x)  #accessing the variable
print(Myclass.x)
print(obj.instan) 
#print(Myclass.instan)  #It will through error becuase there is no attribute in Myclass of this name

print(obj.y) #It will give priority to instance attribute first than it will go to class attribute
print(Myclass.y) # Class attribute changed
# to change class attribute use classname.attribute

Myclass.z=15  #TO add class attribute will automatically added to all its objects
print(Myclass.z)
print(obj.z)