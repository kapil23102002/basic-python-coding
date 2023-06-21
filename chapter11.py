#  *************   INHERITANCE   *************

class Employee(): # Base Class, Parent class
    company = 'Google'

    def Details(self):
        print(f'this is an employee whose working on {self.company}')

class Programmer(Employee): #child class, derived class
    language = 'Python'

    def getLanguage(self):
        print(f'this is an employee whose working on {self.language}')

    # def Details(self):
    #     print(f'this is an employee who are not working on {self.company}')

e = Employee()
e.Details()
p = Programmer()
p.Details()
print(p.company)

#  **********  TYPES OF INHERITANCE   **********

# (1) Single Inhertance (uper vala --- it has only one parent class)

# (2) Multiple Inheritance (More Than one parent Class)

class Manager:
    company = 'Facebook'
    eCode = 93


class Employee:
    company = 'whatsapp'
    level = 2

    def upgrade(self):
        self.level = self.level + 1


class Programmer(Manager, Employee):
    name = 'kapil'

p = Programmer()

p.upgrade()
print(p.level)
print(p.company)
print(p.eCode)

# (3) Multi level Inheritancex (child class become an parent class)
class Gfather:
    country = 'India'

    def occp(self):
        print('He is a Post Master')

class Father(Gfather):
    city = 'Bhopal'

    def occp(self):
        print('He is an Engineer')

    def getSalary(self):
        self.getSalary = 5000

        print(f"salary is {self.getSalary}")

class Child(Father):
    city = 'Indore'

    def occp(self):
        super().occp ()  # it just print first to parent class than itself
        print('He is a Software Engineer')

    def getSalary(self):
        print(f"No salary in this Field")

g = Gfather()
print(g.country)
f = Father()
f.occp()
print(f.country)
f.getSalary()
c = Child()
c.occp()

#  ****** CLASS METHOD *******
class Employee:
    company = 'Apple'
    salary = 100

    # def changeSalary(self, sal): #change class attributes without instance attributes
    #     self.__class__.salary = sal
    #         # OR
    @classmethod
    def changeSalary(cls, sal): #change class attributes without instance attributes
        cls.salary = sal

e = Employee()
print(e.company)
print(e.salary)
e.changeSalary(500)
print(e.salary)
print(Employee.salary)

#  ****** Getter (property method)  and Setter *******
class Employee:
    salary = 5000
    salaryBonus = 1200

    @property # getter method
    def total_salary(self):
        return self.salary + self.salaryBonus
    
    @total_salary.setter #  setter method 
    def total_salary(self, val):
        self.salaryBonus = val - self.salary 

e = Employee()
print(e.total_salary)
e.total_salary = 5700 
print(e.total_salary)
print(e.salaryBonus)

#  ****** OPERATER OVERLOADING  (Dender method) ****** 

class number :
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        breakpoint()
        print('Lets add...')
        return self.num + num2.num
    
    def __mul__(self, num2):
        print('Lets Multiply...')
        return self.num * num2.num
    
    def __truediv__(self, num2):
        print('Lets Divide...')
        return self.num / num2.num

    def __str__(self):
        return f"The number is {self.num}"
    

n1 = number(4)
n2 = number(2)
sum = n1 + n2
# mul = n1 * n2   
# div = n1 / n2
# print(sum)
# print(mul)
# print(div)
   
# n = number(78)
# print (n)