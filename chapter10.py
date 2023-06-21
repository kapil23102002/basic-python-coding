# # *************  OOPS  *************  

# # 1 . class attributes
# class Employee():
#     company = "Google" # class attributes
#     salary = 100
# kapil = Employee()
# rohit = Employee()
# print(kapil.company)
# print(kapil.salary)

# # 2. Instance attributes
# class Employee():
#     company = "Google"
#     salary = 100
# kapil = Employee()
# rohit = Employee()
# kapil.company = ('Amazon') # instance Attributes
# print(kapil.company)
# print(rohit.company)
# # print(rohit.address) throws an error becoz address is not present in class/Instance attributes

# # with "self" we use class/ Instance both attributes
# class Employee:
#     company = "Facebook"
#     def printData(self):
#         print(f"Company Name is {self.company} and it will pay {self.salary}")
#         print(f"Head Office in {self.city}")
# kapil = Employee()
# kapil.salary = "1000"
# kapil.city = "Bhopal"
# kapil.printData()


# # 3. without "self" we use static method
# class RalwayForm:
#     name = "kapil"
#     @staticmethod
#     def printData():
#         print(f"Name is kapil")
#         print(f"Train is Bhopal Intercity")
# kapil = RalwayForm()
# kapil.printData()

# # (construtor) init function (it is no need to print any data)
# class Family:
#     def __init__(self, name, father, mother, brother):
#         self.name = name
#         self.father = father
#         self.mother = mother
#         self.brother = brother
#         print('Family detailed is filled')

#     def Details(self):
#         print(f"Myself {self.name}")
#         print(f"My father name is  {self.father}")
#         print(f"My mother name is {self.mother}")
#         print(f"My brother name is {self.brother}")
# kapil = Family('kapil Bhati', 'Brajendra Singh Bhati', 'Rekha Bhati', 'Rohit Bhati')
# kapil.Details()

# # ques(1) create a class programmer for storing information of few programmers working at microsoft 
# class Employee:
#     company = 'Microsoft'
#     salary = 1000
#     def __init__(self, name, product):
#         self.name = name
#         self.product = product
#     def Info(self):
#         print(f"the name of Company is {self.company}, Programmer is {self.name} and he is working on product is {self.product}")
# kapil = Employee('kapil', 'Excel Sheet')
# shubham = Employee('shubham', 'skype')
# kapil.Info()
# shubham.Info()

# # ques(2) create a class calculator to find sqr , cube , sqr root 
# class Calculator:
#     def __init__(self, num):
#         self.number = num
#     def cal(self):
#         print(f"The square of {self.number} is {self.number **2}")
#         print(f"The cube of {self.number} is {self.number **3}")
#         print(f"The square root of {self.number} is {self.number **.5}")
# number = Calculator(9)
# number.cal()

# # ques(3) class attributes is change or not 
# class Sample:
#     a = "kapil"
# obj = Sample()
# obj.a = "rohit"
# print(Sample.a)
# print(obj.a)

# # ques(4) Ticket booking method
# class Train:
#     train = 'Bhopal InterCity'
#     def __init__(self, name, fare, seats):
#         self.seats = seats
#         self.fare = fare
#         self.name = name 
 
#     def status(self):
#         print("*********")
#         print(f"The name of the train is {self.name}")
#         print(f"The seats available in the train is {self.seats}")
#         print("*********")


#     def price(self):
#         print(f"The price of the ticket is {self.fare}")

#     def bookTicket(self):
#         if (self.seats>0):
#             print(f"Your Ticket has been booked...Your seat no. is {self.seats}")    
#             self.seats = self.seats - 1
#         else: 
#             print("Sorry,  The train is full...!!" )
    
#     @staticmethod
#     def greet():
#         print('*****Welcome to the Railway Vibhag*****')

# kapil = Train('Bhopal InterCity', 110, 2)
# kapil.greet ()
# kapil.status ()
# # kapil.bookTicket ()
# kapil.bookTicket ()
# # kapil.status ()
# kapil.price ()
