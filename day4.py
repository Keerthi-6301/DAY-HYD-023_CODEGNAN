`'''
Identity Opeartors --> checks the identity of aan object --a 
'''
'''
a = 5
b = a
print(id(a))
print(id(b))
c = 5
print(id(c))
print(a is c)
print(5 == 5)
'''
'''
a = [1,3,5,6]
b = a
print(id(a))
print(id(b))
c = [1,3,5,6]
print(id(c))
#As we have Lists (Mutable Collection) both c and a lists will have different
#ids where as values are some
print(c is a) #Output False
print(c ==a) #output True
print(a is not c)
'''
'''
#Bitwise Opeartors --> we perform bitwise operations over operands
#& (and) , | (or),^(XOR),shifting opearators (<<,>>)
#Number will be converted to binary format

print(5&3)#both 5 and 3 to be converted binary and bitwise and is performed
print(5|3)#bitwise OR
print(5^3)#bitwise XOR
print(5 and 3)#here and is logical operator check for both experiences
#returns 5 in above case
print(5 or 3)#returns 3 in this case
'''
'''
#LeftShift Operator << ,Right Shift Operator >>

print(5 < 1)#False Comparision
print(5 << 1)#Left shift operation by 1 position
print(5 > 1)#Right shift operation
print(5 >> 1)
'''
'''
print(15 << 2)# convert 15 to binary and perform 2 times left shifiting
print(15 >> 2)# same 2 times right shifting
'''
'''
#Input Formatting -->input(),int(input()),float(input())
#you know -->single input
#2 or 3 inputs -->map()
#group of integers -->list(map(int,input().split(','))

names = input("Enter the names:").split(',')
print(names)

name1,name2 = map(str,input("Enter the Friends Names:").split(','))
print(name1,name2)                            
'''
#Tokens -->Numeric Datatypes -->Operators -->Flow of the program
#Control Block Statements -->they control the flow of the program
#when to execute,how to execute
#Conditional Statements --> if,else,elif(rely on condition to be executed)
#Repetititon Statements(Loops) -->for,while

#conditional statements --> if usage
'''

Syntax

if <condition>:
    statement(s)...
    ......
'''
'''
#age = 15
age = int(input("Enter your age:"))
if age >18:
    print('your age is:',age)
'''
'''
age = int(input("Enter the age:"))
if age>18 and age in [19,20,21]:
          print('your age is',age)
print(age)
#else keyword -->if-else

else:
   statement(s)..

if-else usage as below:

if <condition>:
  statement(s)...
  ....
'''

#vote Elibility ->To check his/her voter eligibilty and give access...
'''
age = int(input("Enter the age:"))
if age>=18:
    print("you have Voter eligibilty and age is",age)
    print("Access Granted")
else:
    age = 18-age
    print("You dont have eligibility as your age is",age,"years")
    print("You need to wait for more",age,"years")
'''
'''
#same case let's use only nested -->if,else
age = int(input("Enter your age:"))
if age>0:
    if age>=18:
         print("you have Voter eligibilty and age is",age)
         print("Access Granted")
    else:
        age = 18-age
        #print("You dont have eligibility as your age is",age,"years")
        print("You need to wait for more",age,"years")
else:
    print("you have entered -ve values/zero enter only +ve")

'''
'''
task : Student marks and grade analayzer
90 - 100 --> 'A'
80 - 89 --> 'B'
70 - 79 -->'C'
60 - 69 -->'D'
50 - 59 -->'E'
'''

marks = int(input("Enter student marks: "))

if marks > 0:
    if marks >= 90:
        print("Grade A")
    else:
        if marks >= 80:
            print("Grade B")
        else:
            if marks >= 70:
                print("Grade C")
            else:
                if marks >= 60:
                    print("Grade D")
                else:
                    if marks >= 50:
                        print("Grade E")
                    else:
                        print("Fail")
else:
    print("Invalid Marks")
                
                      
            
                  






          



























































