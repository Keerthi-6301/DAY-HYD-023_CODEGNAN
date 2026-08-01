'''Student marks and grade analayzer (if-else)
90 - 100 -->'A'
80 - 89 -->'B'
70 - 79 -->'C'
60 - 69 -->'D'
<60 -->Fail
#also -vr cases should not be allowed and marks shouldnt be grater 100
'''
'''
marks = int(input("Enter the marks (1-100):"))
if marks > 0 and marks <=100:
    if marks >=90:
        print("User has secured Grade A")
    if marks >=80 and marks <=89:
        print("User has secured Grade B")
    if marks >=70 and marks <=79:
        print("User has secured Grade C")
    if marks >=60 and marks <=69:
       print("User has secured Grade D")
    if marks < 60:
       print("User has failed,study again")
else:
    print("Enter only +ve values greater than 0 and less than 100")
    '''

#elif keyword ==>if-elif-else
'''
if <condition1>:
   statement(s)......
if <condition2>:
   statement (s).....
   .........
elif <condition3>:
    statement (s)....
    ........
    ........
else:
    statement(s)...
    .......
'''
'''

marks = int(input("Enter the student marks:"))
if marks>100:
    print("Entered values should be greater tahn 1 and less than 100")
elif marks >=90:
    print("User has secured Grade A")
elif marks >=80 and marks <=89:
    print("User has secured Grade B")
elif marks >=70 and marks <=79:
    print("User has secured Grade C")
elif marks >=60 and marks <=69:
    print("User has secured Grade D")
elif marks < 60 and marks >=0:
    print("User has failed,study again")
else:
    print("No negative values")
 '''   
'''
#Voter Eligibility checkcase -->make sure to satisy all possible conditions    
#>=18  and 100-->Access
#<=18 --
#> no of years eligibility should tell
#negative values --> not acceptable

age = int(input("Enter the age:"))
if age>18 and age <=100:
    print('------ User has Vote Eligibility -----')
    print('------ Access Granted -------')
elif age<18 and age >0:
    print('----- User still need to get Vote Eligibility -----')
    print('------ Access need to wait for more',(18-age),'years(s)------')
else:
    print('------Only +ve valus and less than 100 Acceptable----')
#prefer  if-elif-else....
'''
'''
#output -->print() -->we can pass any values also use sep and end
#Output Formatting -->old style formatting (using commas)
#% usage (%f,%d),.format() Usage, fstring notation
a,b = 7,9
print(a)
print(b)
print(a,b)
name = "Codegnan";batch = "Data Analysis"
print(name,batch)#by default sep is having space
print(name,batch,sep=',')
print(name,batch,sep='------->')
#end ='\n',\t -->tab space
print(name,batch,end='\t')
print(a,b,end='')
print("Hyderabad")
'''

name='Codegnan';age=7;batch='DA-023';place='Hyderabad'
'''#Usage of commas
print(batch,'is in',name) #Variables and msg to be separated by comma
print(name,'is in','age is',age,'years')
#Old style formatting --> 5d -->integer,%s-->string,%f-->float
salary = 24253.256
print("His Salary is %d"%(salary))
print("His Salary is %f"%(salary))
print("His Salary is %.1f"%(salary)) #%.1f --> rounding to 1decimal
'''

#.format() usage
print("{} is in {}".format(name,place)) #order matters

#fstring usage (more recommended)

print(f'{name} is in {place}')
print(f'{"Keerthi"} is in {name}')






            
        
