'''
strings -->CaseConversations,searching&Finding,String testing methods,
Replace,Space removal
'''
'''
#Searching,Finding,Replacing,joining...
'''
'''
a = "Codegnan"
print(len(a))
print(min(a))
print(max(a))
'''
'''
b = a.index('g')# it returns the index position
print(b)
c =a.index('n')#it returns only the first occurance
print(c)
d =a.index('n',6)#it returns the next occurance
print(d)
#e=a.index('n',8)#ValueError
#print(e)
#f=a.index('t')#ValueError
#print(f)
#g = a.index('n',1,4)
#print('g')
'''
'''
#rindex() -->returns last occurance
b = a.index('g')
print(b)
c = a.rindex('n') #here 'n' is occuring at 7th index
print(c)
#d = a.rindex('n',8)#it return ValueErorr
#print(d)
'''
'''
#count()-->returns the number of items object is repeating
print('Codegnan'.count('n'))
print('Code'.count('w'))#it returns o as we dont have 'w' in 'Code'
print('Cakshjasaksajs'.count('a'))
'''
'''
#find() -->first occurance but it avoid error returns -1 if substring is
#not found
print('codegnan'.find('r'))#it returns -1
print('codegnan'.find('n'))
print('codegnan'.rfind('n'))
'''
'''
a = "Data"
print(len(a))
for  i in a:
    #print(i)
    print(a.count(i),a.index(i))
 '''
'''
#Replacing,Splitting,Joining

#String are immutable
a = 'Codegnan'
#a[4] ='s'
print(a.replace('g','s'))
print(a)
a = a.replace('g','s')
print(a)
print('fghyujiki#kasjkhfjdyjska#nmasnam'.replace('#',''))
print(a.replace('x','Keerthi'))
'''
'''
a = 'code keerthi python'
print(len(a))
b = a.split()#it default if we have space it splits(returns list)
print(b)
print(len(b))
c = 'code,keerthi,python'
d = c.split()
print(d)
e = c.split(',')
print(e)
'''
'''
#join(iterable) -->concatenate any number of strings

a='code'
b='gnan'
print(a.join(b))
print(b.join(a))
print(' '.join ('Keerthi'))
'''
'''
#String testing methods (boolean)
#isalpha(),isalnum(),isdigit(),issuper(),islower()......

a = 'Codegnan123'
print(a.isalnum()) #returns True for alphanumeric strings else False
b ='Codegnan'
print(b.isalnum())
print(a.isalpha())#returns True only for alpabets 
print('6305647742'.isdigit())
print('2345'.isnumeric())#this has upper edge (numbers,functions,romans)
#startswith() -->how its starting
print('codegnan'.startswith('c'))
print('codegnan'.startswith('g',4))
print('codegnan'.endswith('f'))
'''
'''
print('codegnan'.islower())#returns  True for all lowercase
print('codegnan'.isupper())#returns True for all uppercase
print('Codegnan python'.istitle())
'''
'''
a = 'codegnan'
print(a.strip())
b = input("Enter the string:").strip().lower()
print(b)
'''
#zfill() filling with zerosnas per the given numeric string
print('234'.zfill(4))
print('234'.zfill(7))
#center(),just(),rjust() -->Aligment os strings (check length and then
#modify the width accordingly

print('hai'.center(6))
print('hai'.center(6,'#'))
print('hai'.ljust(6,'#'))
print('hai'.rjust(6,'#'))


































