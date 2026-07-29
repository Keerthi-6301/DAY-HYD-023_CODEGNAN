'''
Tokens --> Variables,Puncutuators

Variable --> Named memory location,its a placholder for data
#Rules are to be followed
'''
#MultiAssignment of Variables

name,age,place = 'Codegnan',7,'Hyderabad'
print(name,age,place)
print(name,age,place,sep=',')
print(name,age,place,sep='-------->')

#a,b = 2,4,5 #ValueError as too many values to unpack
#Reassigning Variables

name ="Codegnan"
a,b = 45,1.5
print(a,b)
a,b = b,a
print(a,b,sep=',')

#a,b = b,c #NameError as c is not defined
#print(a,b)

#Deleting the variables -->del
#del a
#print(a)
#del a,b
#print(a,b)

#Punctuators --> [](Lists),()(Tuples),{}(Dict,sets)
name = "Codegnan";age = 7;course = 'Data_Analysis'
print(name,age,course)

#DataTypes -->Numeric(int,float,complex),boolean,None,
          #-->Sequences -->Lists,Tuples,Sets,Strings,
           #                 Frozensets,mappings(dict)

#Numeric type -->int,float,complex

#int datatype -->quantity
age = 7
print(age)
print(type(age)) #type -->returns the datatype of object

print(type(234))


#quantity = 03 #it is not allowed
#print(quantity)


#float datatype -->temp,salary,price
price = 750.24;discount = 2.5
print(price,discount)
print(type(price))

#complex -->combination of real and imag
i2 = 4
data = 5 + i2
print(data)

data = 5+2j #j is imag representation
print(data)
print(type(data))

#Boolean -->True / False

valid = True
print(type(valid))

error = False
print(type(error))

#TypeCasting --> Converting one type to another type
#Python by default follows Implict Type (we need not mention the datatype)

#we will go for Explicit Converation

#Every built -in datatype is a built-in function

age = 35
print(type(age))
b = float(age)
print(b)
c = complex(age)
print(c)
d = bool(age)#returns True for existing data
print(d)
e = bool(0)
print(e)

age = 35.5
print(type(age))
b = int(age)
print(b)
c = complex(age)
print(c)
d = bool(age)#returns True for existing data
print(d)



#Float -->TypeCasting -->,complex,bool

price = 750.45
print(type(price))
d = int(price)
print(d)
print(type(d))
e = complex(price)
print(e)
print(type(e))
f = bool(price)
print(f)

#complex -->Typecasting -->int,float,bool
data = 2+5j
print(type(data))
#b = int(data) #TypeError
#print(data)
#c = float(data)
#print(c)
d = bool(data)
print(d)
print(type(d))

e = int(float(bool(45)))

print(e)

e = bool(int(float(25)))
print(e)

f = 45 + 2.5 + 2 + 3j +False
print(f)




           
