#Numeric datatype -->int,float,complex along with boolean
#Input formatting input from the user -->input()
# Accepting integer input from user
#by default input() accepts any input --> str
#int(input()) -->will accept only integers
'''
age = int(input('Enter the age:'))
print(age)
print(type(age))
'''
#float(input()) -->accepts integers,float values
'''
age = float(input('Enter the age:'))
print(age)
print(type(age))
'''
#Accepting string input from user
'''
name = input("Enter the name:")
print(name)
print(type(name))


#Accept group of values
'''
'''
marks = int(input("Enter the marks:"))
print(marks)


a = input().split() #by default split() has space
print(a)

#space separated values

a = input().split() #now you enter spaces in output
print(a)

#comma separated values
a = input("Enter the values:").split(',')
print(a)

#lists of integers
marks = list(map(int,input("Enter the values:").split(',')))
print(marks)'''
'''
#Now we want to accept 2 values from user
age,salary =(map(int,input("Enter the values").split(',')))
print(age)
print(salary)'''

'''
#Single input -->int(input())
#two inputs -->a,b = map(int,input().spliy(','))
#any number result as list --> a = list(map(int,input().split(',')))
a = list(map(float,input("Enter the values:").split(',')))
print(a)
'''

#Accepting input from user --> int,float ->input formatting
#Operators --> Operators perform operations between values(operands)
#7 types -->Arithmatic,Assignement,Comparision (Relationship)
#Membership,Identity,logical,Bitwise
''''
#Arithemetic Operators -->Arithmetic operations
#+,-,*,/
print(5+3)
print(5-3)
print(5*3)
print(5/3) #Float value
#Floor Division (Integer division)-->returns quotient
print(5//3)
#Modlus -->divisible rules ->returns remainder
print(5%3)
#Power (exponential)
print(5**3)
'''
'''
#Task-->Accept integer input as length,breadth -->find the area of rectangle
#Area = length * breath
length =int(input("Enter the values:"))
breath = int(input("Enter the values:"))
Area = length * breath
print(Area)
'''

'''
#Assignment operators -->assign the values
# = ,+= , -=
a = 45
print(a)
#update the value of a
a = a + 5 #a+= 5
print(a)
b = 35
b += a
print(b)
'''
'''
b = 35
print(b)
#update the value of a
b-= 5 #b-= 5
print(b)


#task : *=,/=,//=,%=,**=workout
'''
#Comparision Operators -->we compare the values -->boolean
# == (equal to),!=(not equal to),<(less than),>(greater than)
#<=(less than or equal to)>=(grater than or equal to
'''
age = 25
print(age== 25) #returns Boolean output
print(age != 35)
print(age== 25) 
print(age != 35)
print(age < 25)
print(age >= 25)
print(age > 35)
print(age < 35)
print(-5 < -1)
print(-5 < +1)
'''
#Membership Operators --> in,not in -->boolean
#it checks for the existance of an object in a collection
'''
marks = [56,75,45,85]
print(35 in marks)
#print(35 in 355) #TypeError
print(25 not in marks)
'''


#Logical Operators -->logical decision making -->and ,or,not
#and -->all conditions to be satisfied
#or --> any one condition to be satisified
'''
a = (25 in [25,45,65]) and 45 < 56
print(a)
b = 45 > 56 or 25 <= 45
print(b)
c = not(True)
print(c)
'''

#Identity Operators -->check for identity of an object -->id()
'''
a = 35
b = 35
print(id(a))
print(id(b))
print( a is b)
c = a
print(id(c))
print(c is a)'''

a = [1,3,4,5]
print(id(a))
c = a
print(id(c))
print(c is a)
b = [1,3,4,2,5]
print(id(b))






 


