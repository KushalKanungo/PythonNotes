class Employee:
    company = "Google"

    # It will take parameters while creating an objects(We have to give parameters while creating object)
    def __init__(self, name, salary, star):
        self.name = name
        self.salary = salary
        self.star = star
        print("Init function runs automatically as soon as we create an object")

    def getDetailes(self):
        print(self.name)
        print(self.salary)
        print(self.star)


kushal = Employee("Kushal", 1000, 4)

kushal.getDetailes()
