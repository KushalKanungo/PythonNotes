# self is used in almost all function in  a class util you need to create a function which do not require any atrribute
# self is used for instance attributes

class Employee:
    Comapany = "Google"

    def getSalary(self, star):  # self is used for objects itself
        print("Salary is 100k")
        # self.salary is a instance attribute
        print(f"Salary is {self.salary} working in {self.Comapany} having a ranking: {star} star")

    @staticmethod  # It will convert it in Employee.greet()
    def greet():  # Here we don't want self parameter
        print("Hello Employee")


kushal = Employee()  # Creating Object of a class
kushal.salary = 100000  # Adding instance attribute


kushal.getSalary(5)
# Above is converted to
# Employee.getSalary(kushal)

kushal.greet()
# It will not convert in Employee.greet(Kushal)
# It will convert to Employee.greet() so no need of self
