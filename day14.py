'''

Sequences -->Strings,Lists,Tuples,Sets
Mapping -->Dictionary
'''
'''
#Lists --> Collection og heterogenous elements(items)
#List -->Indexed,Ordered,Mutable,Heterogenous,we use [] to store the data

marks = [35,25,21,45]
print(marks)
print(len(marks))
print(type(marks))
print(45 in marks)

#Operations : Indexing,Slicing,Striding,Membership,Merging,Repetition
'''
'''
#Nested Lists --> A list inside another list
'''
'''
names = ['Codegnan',25,4.6,[45,35,25,65],'DA23',34]
print(names)
'''
'''
print(len(names))
print(names[0])
print(names[3])
print(names[-3])

print(type(names[0]))
print(names[0][:4]) #it returns code
print(names[0][4:])

#get the output as cdga
print(names[0][::2])
names[0] = names[0][::-1]
print(names)
'''
'''
print(names[3])
print(len(names[3]))
print(names[3][2])
#Indexing,Slicing -->Mutable
names[3] = 'python'
print(names)
#By indexing if we change the elements,length of collection will remain same
names[4] = ['codegnan','PFS','JFS','DA','AAA','DS']
print(names)
print(len(names))
print(names[3][1:3])
print(names[4][1:4])
print(names[4][0])
print(names[4][0][4:])
'''
'''
names[2:4] = 'Keerthi','srav','chinnu','lasya'
print(names)
#In Slicing elements u pass as per the logic length keeps on increase

#o/p as follows :
#['Codegnan', 25, 'Keerthi','python', 'chinnu','java','DA23', 34]
names[3:6:2] = ['python','java']
print(names)
'''

#Create a nested list with strings,lists and work on Indexing,Slicing,Striding
#added advantages if u could add string functions also to it
#Lists Functions -->append(),insert(),extend(),pop(),remove(),clear()
#Index(),count(),copy(),sort(),reverse()

names = ['codegnan','keerthi']
#append() -->inserts single elements to the end of the list
names .append('data')
print(names)
#names.append('analysis','agents') #TypeError
names.append(['analysis','agents'])
print(names)
#append() will always increment the length of list by 1
#print(names[3])
#print(names[3].append('chatgpt'))# it returns None as append is applicable
#on list not print
#print(names[3])
print(names)

#extend() -->inserts multiple elements to the end of list
'''
names.extend('analysis')#string wii be splitted
print(names)
names.extend(['analysis'])
print(names)
names.extend([45,75,24,56])
print(names)
#names.extend(35,45) TypeError -->as only 1 argument to be passed..
#print(names)
'''
'''
#insert(index,object) -->inserts given object before index
names.insert(1,'python')
print(names)
names.insert(0,'java')
print(names)
#names.insert([1:4],['a','b'])#SyntaxError
#print(names)
names.insert(-1,'AAA')
print(names)
'''

#pop(),remove(),clear()
#pop(0 by default last,else given index
names.pop()
print(names)
names.pop(2)
print(names)
#remove() we can remove a specific value
names.extend([23,14,15])
print(names)

names.remove(14)
print(names)
#names.remove(14) #it raises ValueError
del names[1:3] #del keyword will apply  permanent changes
print(names)
names.clear() #clear() will remove all elements and returns empty list
print(names)

#Task
#data = ['codegnan','keerthi','python','java',]#input
#output should be as follows
'''
0 : codegnan
1 : keerthi
2 : python
3 : java
'''























































































































































































































































































































































































































































































































































































































































































