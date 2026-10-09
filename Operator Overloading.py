'''
#Operator Overloading -->Operators (+,-,*,/) -->Operator will behave in adifferent way as per user defined object
# + (Addition,Concatenation,Merging)

print(3+4)
print('code'+'gnan')#Concatenation
print([23,45]+[4,5])#Merging
#print(3.__add__(4))
a=25;b=3
a=[12,3,4];b=[3,4,5]
print(a.__add__(b))
print(a.__len__())
print(a.__mul__(2))

#let's apply the above scenario Hotstar WatchHistory

class   WatchHistory:
    """Define the number of hours"""
    def __init__(self,hours):
        self.hours = hours
varun = WatchHistory(100)
print(varun.hours)
akash = WatchHistory(120)
print(akash.hours)
#print(varun+akash)#TypeError unsupported operation
print(varun.hours+akash.hours)
'''
'''
#But the prederable way is usage of __add__()
class WatchHistory:
    """Define the number of hours"""
    def __init__(self,hours):
        self.hours = hours 
    def __add__(self,other):
        return self.hours + other.hours
    def __str__(self):
        return f'WatchHistory is {self.hours}'  
varun = WatchHistory(300)
print(varun) #__str__() method
akash = WatchHistory(50)
print(akash)
print(varun + akash)  
'''         