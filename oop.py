"""
Object Oriented Programming: 
- Paradigm => a way to author your code for reusability
- we majorly create *class* => blueprint of an object
- from the class we get an Object( a instance of class)

class: Blueprint ot create an object
object: an instance of a classs

Polymorphism => many forms 
Inheritance =>
Encapsulation => "hide what is needed to be hidden and show what is meant to be shown"

"""

name ="JOhn DOe" # instance of a string....
name.upper()

#  blueprint
class Animal:
    #  attributes
    name = "Bosco"
    color =  "Brown"

    # method 
    def bark(self):
        print("Whvoof!")
    
    def name(self):
        print("My name is Bosco")

#  creating the real world thing

# animal1 = Animal() # creating a real object
# animal2 = Animal() # creating a real object
# animal1.bark()
# animal1.name()
# animal2.bark()


class Human:

    def __init__(self, name, age, height, hobby):
        self.name = name
        self.age = age 
        self.height = height
        self.hobby = hobby
    
    def thinking(self):
        print(f"My name is {self.name} and I am thinking!")

    def drinkWater(self):
        print(f"My name is {self.name} and I am drinking water!")
    
    def consumeFood(self):
        print(f"My name is {self.name} and I am eating!")





class Student(Human):
#  initialization
    def __init__(self,name, age, height, hobby, course): 
        super().__init__(name, age, height, hobby)
        self.course = course     

    def introduction(self):
        print(f"Hello! My name is {self.name.upper()} and I am {self.age}yrs old!")

    def courseName(self):
        print(f"I am currntly pursuing {self.course}")

    def consumeFood(self):
        print(f"My name is {self.name}, I pursure {self.course} and I am eating!")


student1 = Student("Jane Doe", 12, 100, "reading", "coding")
student2 = Student("John Wilson",18, 100, "reading", "coding")
student1.drinkWater()
student1.consumeFood()
# student1.introduction()
# student1.courseName()
# student2.introduction()
# student2.courseName() 


# class Account:
#     #  initialization
#     def __init__(self, name, age, user_id,balance, loans):
#         self.__name = name # encapsulation
#         self.age = age 
#         self.user_id = user_id    
#         self.balance  = balance
#         self.loans = loans 
        
#     def accountDetails(self):
#         print(f"Accnt Name: {self.__name}")
#         print(f"Accnt ID: {self.user_id}")
#         print(f"Accnt Balance: Ksh. {self.balance} /=")
#         print(f"Accnt Loans: {self.loans}")

#     def getBalance(self):
#         print(f"Your current balance is {self.balance}")


# account1 = Account("Jane", 12,12345, 300.05, 0)
# account2 = Account("Doe", 18,23456, 123456789, 100000)
# account3 = Account("Kim",21,1098765, 123456789000, 10)

# account1.accountDetails()
# print(f"Dear {account1.__name}, your current balance is Ksh. {account1.balance}/=")
# print(f"Dear {account1.name}, your current balance is Ksh. {account1.balance}/=")
# print(f"Dear {account2.name}, your current balance is Ksh. {account2.balance}/=")
# print(f"Dear {account3.name}, your current balance is Ksh. {account3.balance}/=")