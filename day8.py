'''
Tokens -->Keywords,Identifiers,Literals,Operators,Punctuators,Variables
operators -->Numeric data (int,float,complex),bool
Control Flow -->if,else,elif,for while
Sequences -->Strings,lists,sets,tuples,mapping(dict)
'''

#Strings -->Group of characters,we use single or double or triple quotes
#for representation of strings...
#Strings are Immutable,Ordered,Indexed,Collection
#space is also a character
'''name ='Codegnan'
print(name)
'''
'''print(type(name))#len -->returns the number of items in container
print(len(name))
'''
'''
#index() -->fetch the object (position) starts at 0 and ends at len(obj)-1
#we use [] representation
print(name[0])
print(name[5])
#print(name[25]) #IndexError --> as its out of range

#Negative Indexing --> -1 to len(obj)
print(name[-1]) #It returns last character
print(name[-3])
#print(name[-33]) #IndexError
'''
'''
#Slicing --> We can access group of characters(objects)
#we use [start:end] #start default --> 0,start is included,end is excluded

print(name[:]) #returns entire string
print(name[:5]) #returns entire string
print(name[:4])#starts at 0th index before 4th index
print(name[1:5])
print(name[0:5])
print(name[4:])
print(name[:0])
print(name[0:])
'''
'''
name ='python'
''''''print(name[7:3])#returns empty  as strings are immutable
print(name[3:7])
#Slicing is applicable from lower index to higher index
print(name[:45])#returns till end of the string
print(name[45:])
'''
'''
print(name[-1:-5])#returns empty string
print(name[-5:-1])#starts at -5 and ends at -2
#print'on'from above string
print(name[4:])
print(name[4:6])
print(name[-2:])

print(name[1:-2])
print(name[2:-6])
#observe +ve,+ve, -ve,-ve all possibilites
'''
'''
#Striding -->[start:end:step]

course = 'DataAnalysis'
print(len(course))
#Data -->result
print(course[:4])
print(course[4:])
print(course[-3])

print(course[::1]) # returns all characters
print(course[::2]) #include start to end skipping 1 character
print(course[1:6:3]) #[1:6] -->ataAn -->[1:6:3] -->aA
print(course[2::3])
print(course[::-1]) #it returns the reverse of a string
print(course[::-2])
'''
'''
#task:workout with all possibilities os slicing and striding on a example
name = 'codegnan'
#name[3] = 'w' #String are immutable

#Operations on String -->Indexing,Concatenation,Repetition
print(name * 3)
print('*' * 25)#repetition

#Concatennation -> combining strings

data = 'keerthi' + 'python' + ' ' + 'database'
print(data)
print('123' * 4)#Numeric String
print('code' in 'codegnan')


for i in 'codegnan':
    print(i,':')
    
# in above case we get every character line by line
'''
'''
for i in 'codegnan':
    print(i,end=' ')
    '''
'''
name = "dataCodegnan"
#Bulit-in functions -->len(),max(),sorted()
print(len(name))
print(min(name))# alphabetical order ASCII ordering
print(ord('A'))
print(ord('a'))
print(max(name))
print(chr(97))
print(max(name))
print(sorted(name)) #returns a list by sorting all elements
'''
#Methods on Strings -->Case-Conversions,Finding/Searching...
name = 'Codegnan data'
#Case-Conversions -->upper(),lower(),title(),capitalize()
a = name.upper()
print(a)
b = name.lower()
print(b)
#Capitalize() -->converts first letter to uppercase
c = name.capitalize()
print(c)
d = name.title()#converts every work first letter to uppercase
print(d)

#Task : A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
#Use loops and strings to return A - Z




































































































































