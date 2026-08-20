'''
Functions -->Arguments Usage (variable length arguments)
          -->keyword variable length arguments (**kwargs)
Exception Handling / scope of variables / bulit -in functions
Exception Handling -->bit is a mechanism that helps to respond or make the flow of execution and normal way,without this errors will occur and disrup the flow of program

common Exceptions -->ValueError,TypeError,IndexError,AttributeError
ZeroDivisionError...

Syntax:

try:
  #code that will cause the exception
except Exception as e:
    #code will catch the exception
finally:
    #runs irrespective of try/except...
    ....

#basic Exception handling
try:
    #a = 10
    a = int(input("Enter the value"))
    result = 20/a
    print(result)
#except Exception as e:
    #print(e) # it returns the msg of error
except ValueError: #check by changing case
    print(f"Invalid entry enter only integer value")
except ZeroDivisionError:
    print(f'Division by Zero is not possible')
except NameError:
    print(f'Check the name of variable properly')

#Similarly if we want to check other Errors ->IndexError,AttributeError

try:
    a = [10,20,30]
    print(a[5])
#except Exception as e:
    #print(e)#returns the message of Error
except IndexError:
    print(f'Check the length of list properly and access elements')
except AttributeError:
    print(f'Dont rush write the name properly')

#handling exceptions at a time
try:
    a = [10,20,30]
    a.append(24)
    print(a[5])   
except (IndexError,AttributeError)as e:
    print(e)
    a = list(map(int,input("Enter").split(','))) #only for understanding
    print(a)         

#BMI -->bmi = (weight) / (height)**2)
#Feet -->12 inches -->1 inch ->2.54cm
while True:
    try:
        weight = int(input("Enter the weight in kgs:"))
        height = float(input("Enter the height in metres:"))
        #write my logical condition
        if weight > 0 and height > 0:
            break#stops the flow of excution of program
            #continue#skips the current iteration and proceed for rmng iteration
        
            #print("Bye")
        else:
            print("Make sure to enter only correct values")
    except ValueError:
         print(f'Make sure to enter weight as integer only,height also as number')
bmi = ((weight) / (height)**2)
print(bmi)


#Use Exception Handling along with jumping Statement in
#Functions BmI Task
'''

#Scope of variables --> Scope is basically the region/area where it is
#accessible
#Local Scope,Global Scope
#Global Keyword,Enclosing Scope(Nested Functions nonlocal keyword)


#Local Scope -->variables defined inside the function accessible inside
'''
def display():
    """Usage of Local Sscope"""
    name = "Codegnan"#local variable
    print(name)
display()
#print(name)#it raises NameError

#Global Scope(variables) -->Defined outside and can be accessible anywhere
#in the script
place = "Hyderabad"
def display():
    """Usage of Local Sscope"""
    name = "Codegnan"#local variable
    print(f'{name} is in {place}')
display()
print(place)


#Modifing global variable inside the function and accessible outside the function

count = 20
def data():
    """Usage  of global keyword """
    global count 
    count = count + 5
    print(f'Value inside function is {count}')
data()
print(f'Value outside function is {count}')
    

#Local variable has high priority over global variable
count = 20
def data():
    """Priority of  local vs global varible"""
    count = 5 #local varaible
    count = count + 5
    print(f'Value inside function is {count}')
data()
print(f'Value outside function is {count}')
    

#Enclosing Scope (nonlocal keyword)
def outer():
    """Outer function with local variable"""
    count = 5
    def inner():
        """Nested Function"""
        nonlocal count
        count = count + 10
        print(f'Value inside is {count}')
    inner()
    print(f'value outside is {count}')
outer()   
'''
#Built-in functions -->variables builtinScope
len = 56
print(len+4)
print(len('codegnan')) #TypeError --> Never ever use Bulitin functions as Identity































































