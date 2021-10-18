# Inheritance is a way of creating a new class from an existing class

class Employee:  # Parent Class
    company = "Google"

    def showDetails(self):
        print("This is an employee")


class Programmer(Employee):  # Child class it will have all the attributes and methods from parent class
    language = 'Python'
    company= "Youtube"

    def getLanguage(self):
        print(f"The language is {self.language}")


e = Employee()
e.showDetails()

p = Programmer()
p.getLanguage()
p.showDetails()  # Fetching from parent class is two methods are same it will give priority to child class


# Types of inheritance

# 1. Single Inheritance ---> When a child class inherit from a single parent class
# 2. Multiple Inheritance ---> When a child class inherit from more than one parent class
# 3. Multilevel Inheritance ---> When a child class becomes parent class for another class 



