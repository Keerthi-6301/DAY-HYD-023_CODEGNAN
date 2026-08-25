'''
class Father:
    """Usage of Constructor in Single Inheritance"""
    def __init__(self,property):
        self.property = property
    def father_property(self):
        print(f'Father Property is {self.property}') 

#class Kid(Father):
    #pass
class Kid(Father):
    """Now childclass will have Constructor"""
    def __init__(self,cash,property):
        self.cash = cash
        super().__init__(property) #calling superclass constructor
    def kid_property(self):
        print(f'Kid Property is {self.cash}') 
        print(f'kid Final Property is {self.cash + self.property}')       
obj = Kid(250000,100000)
obj.kid_property()

#whatif child class is having same method name as
# parent class -->Method Overriding
# Area of Square/Rectangle

class Rectangle:
    """Method Overriding usage"""
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        print(f'Area of Rectangle is {self.x * self.y}')
class Square(Rectangle):
    def __init__(self,x):
        self.x = x
    def area(self):
        print(f'Area of Square is{self.x**2}')
obj = Square(7)
obj.area() 
# obj.rarea() #raiseattribute error                    

class Square:
    """Method Overriding usage"""
    def __init__(self,x):
        self.x=x
    def area(self):
        print(f'Area of Square is {self.x **2}')
class Rectangle(Square):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        super().__init__(x)
        
    def area(self):
        super().area()
        print(f'Area of Rectangle is{self.x * self.y}')
x,y = map(int,input("Enter the values:").split(','))
obj = Rectangle(x,y)
obj.area()
'''
'''#multiple Inheritance
class Parent1:
    .....
class Parent2:
    .....
class child(parent1,parent2):
    .....

class user:
    """First parent class with user features"""
    def  voice_call(self):
        print('Making Voice Calls')
class Notifications:
    def notification(self):
        print("Sending Notifications..")
class Premiumuser(user,Notifications):
    def verification_badge(self):
        print("Blue Tick Verification done") 
user = Premiumuser()
user.verification_badge()
'''
#Multilevel Inhertitance -->level by level
'''
class GrandParent:
    .....
class Parent(GrandParent):
    .....
class child(parent):
    .....
'''
class User:
    def user_details(self):
        print("User details")
        print("Name: Keerthi")
        print("Email: keerthi@gmail.com")


class BusinessUser:
    def business_details(self):
        print("Business User")
        print("Business Name: codegnan Company")
        print("Business Type: Data Analyst")


class VerifyBusinessUser(User, BusinessUser):
    def verify(self):
        print("Business User Verified")


obj = VerifyBusinessUser()

obj.user_details()
obj.business_details()
obj.verify()