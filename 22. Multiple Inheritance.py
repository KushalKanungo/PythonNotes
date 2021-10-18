class Employee:
    company = "Google"
    eCOde = 120

    @staticmethod
    def greet():
        print("Hello Employee")


class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level+1

    @staticmethod
    def greet():
        print("Hello Freelancer")


# Priority vise Employee first, this child class has two parent class
class Programmer(Employee, Freelancer):
    name = "Kushal"


p = Programmer()
f = Freelancer()
e = Employee

p.upgradeLevel()
print(p.level)
print(p.company)

print(f.greet())
