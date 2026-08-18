'''
Tokens,Datatypes -->Control Flow Statements -->if,elif,else,for,while,break
continue...

Procedure Oriented programming

Functions --> A function is a block of code which performs a specific task
Its a reusable group of statements where we define using
def keyword
Advantages -->code reusability,code maintainability,ease of debuggin,
avoiding code duplication,modularity

def fname(parameters): Function defn
    """Doc String""" Description
    statement(s).......
    ..........           Function body
    return value(s).....
fname(args)    Function call

'''
#To perform sum of given objects
'''def add(a,b):
    """Sum of objects"""
    c = a+b
    return c
print(add(12,3)) #Addition
print(add('code','gnan')) #concatenation
print(add([12,5],[12,34])) #Merging
c,d = map(int,input("Enter the values:").split(','))
print(c,d)
print(add(c,d))


def add(a,b):
    """Sum of objects without return"""
    print(a+b)
add('code','gnan')
print(add(12 ,-34))# it returns result along with None

name,age,salary = "Saketh",32,50000
#usage of return

def details():
    #return name,age,salary
    #return "Codegnan"
    #return 23+34+45
    return     # it return None as output
print(details())

There are 5 types of aruguments:
-->Positional Arguments
-->Default arguments
--> keyword arguments
-->Variable length arguments (*args)
--> keyword variable length arguments (**kwargs)

#Positional Arguments -->Number of arguments in function defn should
#match with function call (order has to be maintained)
#print(len(123,234)) this is a per built -in len(obj) will accept one argument

def details(name,place):
    """To store the details"""
    #name = "Codehnan"
    #place = "Hyderabad"
    #return name,place
    print(f'Name is {name}')
    print(f'Place is{place}')
#print(details("Saketh","Codegnan"))
#print(details("sai","vizag"))
#print(details("vizag","shyam",34))#raises TypeError as only 2 arguments to
c,d = map(str,input("Enter the values").split(','))
details(c,d)

#Default arguments --> we can make arguments as default but not first arguments
#as default

#def grocery(item,price =35):
#def grocery(item = "Cheese",price = 100): #we can also make all args as default
#def gerocey(item ="Burger",price): #non default always follows default
    """usage of default arguments"""
    print(f'The Item is {item} and price is {price}')

grocery("Milk",32)
#grocery(32,"Milk")
grocery("Bread")# by default we have given price as 35
grocery() #as bothnitem and price as default arguments
'''

#keywords arguments --> Whenever we want to sepcify the same of argument
def employee(name,salary,role,place ="Codegnan"):
    """Keyword arguments usage"""
    print(f'Employee name is {name}, role is {role} and salary is {salary},works in{place}')
employee("sai",20000,"Admin")
employee(salary = 25000,role = "Frontdesk",name= "Asha")
employee("Akash",250000,"IT","Cognizant")











































































