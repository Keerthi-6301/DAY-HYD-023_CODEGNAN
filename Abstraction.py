'''
OOP -->class(attributes,methods (constructor,Instance Method)),
object creation/utilisation -->Encapsulation,Inheritance,polymorphism
OOP -->Abstraction,Usage of class methods,Static Method

#Class methods -->these are termed by using @classmethod decorator
# It applie for entire classlevel data,thereby every object utlisation
will be modified..

#lets on an example related to Ecommerce

class Ecommerce:
    """Usage of classmethod & class attribute"""
    company = "Flipcart" #class attribute
    delivery_charge = 50 #class attribute
    @classmethod
    def update_delivery(cls):
        cls.delivery_charge = 100
        print(f'New Delivery Charges {cls.delivery_charge}')
Product = Ecommerce()
print(Product.company)
print(Product.delivery_charge)
print(Ecommerce.company) #classattributes can be directly accessed using class name
print(Ecommerce.delivery_charge)
Product.update_delivery() #accessing classmethod
print(Product.delivery_charge)
Moblie = Ecommerce()
print(Moblie.delivery_charge) 

#Applying Inheritance and usage of classmethod,classattributes
# banking scenario -->RBI -->SBI,HDFC....
class RBI:
    """Inheritance usage and Classmethod"""
    available_cash = 5000000 #classattribute
    @classmethod
    def rbi_cash(cls):
        print(f'Available Cash with RBI is {cls.available_cash}')
class SBI(RBI):
    pass
a = SBI()
print(a.available_cash)
a.rbi_cash()
SBI.rbi_cash()

class HDFC(RBI):
    """Inheritance usage and Classmethod"""
    cash = 3000000 
    @classmethod
    def hdfc_cash(cls):
        print(f'HDFC cash is {cls.cash}')
        #print(f'Total cash is {cls.cash+cls.available_cash}')
        print(f'Total cash is {HDFC.cash + RBI.available_cash}')

#a = SBI()
#print(a.available_cash)
#a.rbi_cash()
#SBI.rbi_cash() #we can also access with classname directly
b = HDFC()
print(b.available_cash)
print(b.cash)
b.rbi_cash()
b.hdfc_cash()       

class RBI:
    """Inheritance usage and Classmethod"""
    cash = 5000000 #classattribute
    @classmethod
    def rbi_cash(cls):
        #print(f'Available Cash with RBI is {cls.available_cash}')
        print(f'Available cash with RBI is {RBI.cash}')
class SBI(RBI):
    pass        
class HDFC(RBI):
    """Now we will aslo add some cash to it"""
    cash = 3000000 
    @classmethod
    def hdfc_cash(cls):
        print(f'HDFC cash is {cls.cash}')
        print(f'Total cash is {cls.cash + RBI.cash}')
a = HDFC()
print(a.cash)
a.hdfc_cash()
a.rbi_cash()

#If incase as above scenario we have same name for class attributes in
#both parent and child classes,the best approach is to call
#the class attributes is using class names such as (RBI.cash)

#we can create it using @staticmethod decorator
#it is mainly used as utility or helpher functions

class Ecommerce:
    """Usage of Static Method"""
    @staticmethod
    def free_delivery(price):
        return price>500
u1 = Ecommerce()
print(u1.free_delivery(450))
print(u1.free_delivery(1000))

#Now lets relate both class method and staticmethod in a single used
class Ecommerce:
    """Usage of class&static method"""
    platform = "Flipkat" #classattribute
    @classmethod
    def show_platform(cls):
        print("Welcome to the Platform;")
        print(f'{cls.platform}')
    @staticmethod
    def free_delivery(price):
        #return price>500
        if price > 500:
            print("You are eligible for Free Delivery")
        else:
           print("You need to pay Delivery charges")
user = Ecommerce()
#print(user.platform)
user.show_platform()
print(user.free_delivery(450))
print(user.free_delivery(1200)) 
''' 
#Abstraction :It aslo on of the key feature of OOP,where it shows 
# only the relevent details to the user and hides the implementation feature
# Instagram -->Uploading photo,Upload video,Reel
#when we need all child classes to follow same pattern
# we have abc module to implement abstraction

import abc
from abc import ABC,abstractmethod 
class Content(ABC):
    @abstractmethod
    def upload(self):
        pass 
class Photo(Content):
    '''def upload(self):
        print("Compressing the Picture")
        print("Edit the Picture")
        print("Photo uploaded successfully")'''
    pass #as we made upload as abstarct method mandatory it has be follow   
class Video(Content):
    def upload(self):
        print("Encoding the video")
        print("Video Editing is in process")
        print("Video Uploading Successfully")  
class Reel(Content):
    def upload(self):
        print("Adding Effects to the Reel")
        print("Reel is Edited")
        print("Reel is Uploaded Successfully with tags..")
'''Contents = [Photo(),Video(),Reel()]
#print(Contents)
for content in Contents:
    content.upload()'''
#obj  = Photo()
# print(obj) #TypeError as we are not following the upload pattern  
a = Video()
a.upload()                                         