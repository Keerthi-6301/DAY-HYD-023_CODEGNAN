'''
OOP -->Object Oriented Programming -->Objects 
-->Attributes (Data),Methods(Behaviour)
class,object ->A class is a blueprint(template) for an object
An object is an instance (physical thing) which utilises the class
object -->An object orirnted programming is mechanism are a process which revolve  around cration objects
attributes  variables --> which carry data to the class
methos -->  A method define inside a class which carry behaviour of the object

Ecommerce Platform
-->Mobiles -->Price,Features(Camera,Storage,RAM)
-->Variables,def moblie()
-->Laptops -->Price,Features
-->Gadgets -->Price,Features
-->variables,def gadgets()
-->Electronic Items -->price,features
-->variables,def elect()
Features  of OOP --> Modularity,Scalability,
Encapsulation(binding the data(attributes).features to the class)(object)
Abstraction -->Show only relevant information to the class
Inheritance -->Acquring properties (attributes,methods)
single -->Fingerprint
multiple interitance -->Parents(mother,father) -->child
multilevel -->GrandParent -->parent -->child
polymorphism -->Method Overloadding,Method Overriding,
operator Overriding
'''

#Syntax for class creation:
'''
class Class_Name:
    """ Doc String"""
    attributes (characteristics)
    ...........
    def func(self):
        .......
        .......
   ......
obj = Class_Name()

#Student Class with basic details
class Student:
    """Understanding the usage of OOP"""
    name = "Keerthi"
    id = "CGH2309"
    gender = "female"
    email_id ="keerthi@gmail.com"
    #Methods(behaviour)
    def display(self):
        print(f'Student name is {self.name}')
        print(f'Student ID is {self.id}')
        print(f'Student Mail id is {self.email_id}')
u1 = Student()
print(u1) 
#print(dir(u1))  #directory (returns all available methods/attributes class)  
print(u1.display()) 
u2 = Student()
u2.display()  

#Student class for multiple objects
class Students:
    """Understanding the usage of OOP"""
    name = input("Enter the name:")
    id = input("Enter the ID No:")
    gender = input("Enter the Gender")
    email_id =input("Enter the Mail id:")
    #Methods(behaviour)
    def display(self):
        print(f'Student name is {self.name}')
        print(f'Student ID is {self.id}')
        print(f'Student Mail id is {self.email_id}')
u1 = Students() 
u1.display()
u2 = Students()
u2.display()  
print(u1.__dict__) # it returns empty dict
print(u2.__dict__)# it returns empty dict
'''
#Students details with multiple objects
class Students:
    """Understanding the usage of OOP"""
    def data(self,name,id,gender,email_id):
        self.name = name
        self.id = id
        self.gender = gender
        self.email_id = email_id
    #Methods(behaviour)
    def display(self):
        print(f'Student name is {self.name}')
        print(f'Student ID is {self.id}')
        print(f'Student Mail id is {self.email_id}')
u1 = Students() 
u1.data("Keerthi","CGH2309","Female","keerthi@gmail.com")
u1.display()
print(u1.__dict__)
u2 = Students()
u2.data("Akash","CGH2304","Male","akash@gmail.com")
u2.display()
print(u2.__dict__)

#Create a class with Car Brand name,price,color -->display()
class Car:
    def data(self, brand,name, price, color):
        self.brand = brand
        self.name = name
        self.price = price
        self.color = color

    def display(self):
        print(f"Car Name:{self.name}")
        print(f"Car Brand: {self.brand}")
        print(f"Car Price: {self.price}")
        print(f"Car Color: {self.color}")

c1 = Car()
c1.data("Fortuner","Toyota", 1000000,"Red")
c1.display()

c2 = Car()
c2.data("Creta","Hyundai", 800000, "Black")
c2.display()