'''
Constructor -->It isa sepical method 

class Cars:
    """Understanding the usage of Constructor"""
    def __init__(self, brand,name, price, color):
        self.brand = brand#public attributes
        self.name = name
        self.price = price
        self.color = color
        #Methods(behaviour)

    def details(self):#Instance method
        print(f"Car Name:{self.name}")
        print(f"Car Brand: {self.brand}")
        print(f"Car Price: {self.price}")
        print(f"Car Color: {self.color}")

u1 = Cars("Tata","Nexon", "8Lakhs","Blue")
u1.details()


class Cars:
    """Understanding the usage of Constructor"""
    def __init__(self):
        self.brand = "BMW"
        self.name = "Sedans"
        self.price = "50Lakhs"
        self.color = "White"
        #Methods(behaviour)

    def details(self):
        print(f"Car Name:{self.name}")
        print(f"Car Brand: {self.brand}")
        print(f"Car Price: {self.price}")
        print(f"Car Color: {self.color}")

u1 = Cars()
print(u1.brand,u1.name,u1.color,u1.price)
u1.details()

Encapsulation -->It is main feature of OOP.
It binds (bundles) the data (attributes) and the methods (behaviour) 
into a single unit(class) -->multiple objects
-->Attributes -->Public,Protected,Private
#Public attributes -->Attributes defined inside the class(constructor)
and can be modified outside the class

class CodegnanPortal:
    """Codegnan Portal with Users"""
    def __init__(self,username):
        self.user = username #Public attribute
    #To access student details
    def display(self):
        print(f'Student Username is {self.user}')
u1 = CodegnanPortal("Marakakeerthi")
u1.display()
u1.user = "Maraka keerthi"
u1.display()
print(u1.__dict__)
u2 = CodegnanPortal("jaychandra")
u2.display()
print(u2.__dict__)       

 #Protected attributes -->we use single underscore before an attribute moreover it can be modified aslo outside the class and even accessible in subclass...
class CodegnanPortal:
    """Codegnan Portal with Users"""
    def __init__(self,username,_otp):
        self.user = username #Public attribute
        self._otp = _otp #protected attribute
    #To access student details
    def display(self):
        print(f'Student Username is {self.user}')
        print(f'Student has received OTP as {self._otp}')
u1 = CodegnanPortal("keerthi",23456)
u1.display()
u1._otp = 3456
u1.display()  

#modify
class CodegnanPortal:
    """Codegnan Portal with Users"""
    def __init__(self,username,_otp,password):
        self.user = username #Public attribute
        self._otp = _otp #protected attribute
        self.__password = password #Private attribute
    #To access student details
    def display(self):
        print(f'Student Username is {self.user}')
        print(f'Student has received OTP as {self._otp}')
        print(f'Student password is {self.__password}')
u1 = CodegnanPortal("keerthi",23456,"admin123")
#print(u1.password) AttributeError as password is private
print(u1.__dict__)
print(u1._CodegnanPortal__password) #NameMangling
'''
#In above we are using NmaeMangling but the right way is
#usage of getter() and setter() methods
class CodegnanPortal:
    """Codegnan Portal with Users"""
    def __init__(self,username,_otp,password):
        self.user = username #Public attribute
        self._otp = _otp #protected attribute
        self.__password = password #Private attribute
   #Usage of getter() method  
    def get_password(self):
        return "******"
   #to modify the password we use setter()method
    def set_password(self,new_password):
        if len(new_password) < 6:
           print("Wromg Password not satisfied 6 characters")
        else:
           self.__password = new_password
           print("Now password is updated")         
u1 = CodegnanPortal("Keerthi",23456,"admin123") 
print(u1.get_password())
u1.set_password("Keerthi") 
u1.set_password("Keerthi123") #compulsory morethan 6
print(u1.get_password()) 