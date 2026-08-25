'''
OOP -->Class,Object,Methods (_init__())
Encapsulation --> It is one of key feature of OOP where we inheritance
 the properties (attributes/methods) from one class to another
  class (base class (parent class) --> dervied class) (child class)-->
Whatsapp -->Personal User,Business User (Catalog),Community admin
Features -->Code Reuseability,Avoiding Code Duplication,
code Maintainability,Polymorphism (method Overriding,(super())Method overloading,Opeartor Overloading __add__,__str__)

Types : Single Inheritance(Finger Print)
-->One child class inherting properties from one parent class
Multiple Inheritance (Mother,Father -->Child) -->one child
class inherting properties from two parent classes
Multilevel Inheritance (GrandParent -->Parent -->child)
level by level
Hierachical  Inheritance -->multiple child classes
inheriting properties from single parent
Hybrid  Inhertances -->It can carry one or more type of
 inhertances

Syntax:
Single Inheritance:

class baseclass:
    statement(s)..
    ......
    ....

#whatsapp Scenario -->Personal User


class user:
    """Single Inheritance usage"""
    def send_message(self):
        print('Sending Message')
    def voice_call(self):
        print('Making Voice Calls')
    def video_call(self):
        print("making video calls")
class Businessuser(user):
    #pass 
    def create_catalog(self):
        print("Displaying Products Catalog")
u1 = Businessuser()
print(dir(u1))
u1.send_message()
u1.video_call()
u1.voice_call()

#Social Media Login -->users -->update_users
class users:
    """Single Inheritance uasage"""
    company = "Codegnan" #class attribute
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def full_name(self):
        return self.fname + self.lname
#u1 = users("Keerthi","Maraka")
#print(u1.full_name())
#print(u1.company)
class Update_users(users):
    def update_name(self):
        return self.fname.title()+" "+self.lname.title().strip()
u1 = Update_users("Keerthi"," Maraka")        
print(u1.company)
print(u1.full_name())
print(u1.update_name())
u2 = users("sai","tarigopula")
print(u2.full_name())
print(u2.company)


#What if we have constructor in child calss also...
#Father -->Kid (Property)

class Father:
    """Usage of Constructor in Single Inheritance"""
    def __init__(self):
        self.property = 100000
    def father_property(self):
        print(f'Father Property is {self.property}') 

#class Kid(Father):
    #pass
class Kid(Father):
    """Now childclass will have Constructor"""
    def __init__(self):
        #self.property = 200000
        self.cash = 2000000
    def kid_property(self):
        print(f'Kid Property is {self.cash}')        
obj = Kid()
obj.father_property()
obj.kid_property()
#In above case it is giving same value for Father also as 
# 2 lakhs ..when we gave property as same attribute in both class
# parent class is having constructor or child is having constructor so constructor overriding is happining..     
# to avoid construct overriding to start super() overriding...
# super(). __init__()
# super().__init__(args)
#super().method() method overriding
# one of the princple of polymorphism 
'''
#In the above case

class Father:
    """Usage of Constructor in Single Inheritance"""
    def __init__(self):
        self.property = 100000
    def father_property(self):
        print(f'Father Property is {self.property}') 

#class Kid(Father):
    #pass
class Kid(Father):
    """Now childclass will have Constructor"""
    def __init__(self):
        self.cash = 2000000
        super().__init__() #calling superclass constructor
    def kid_property(self):
        print(f'Kid Property is {self.cash}') 
        print(f'kid Final Property is {self.cash + self.property}')       
obj = Kid()
obj.father_property()
obj.kid_property()
    


     