#Task:Take a user input as string,do this in two ways..
'''
1) give the count of each repeating character
Test case 1 :programming

r is repeating 2 times
g is repeating 2 times
m is repeating 2 times
s = input()
'''
'''
s = input()
for ch in s:
    if s.count(ch) > 1:
        print(ch, "is repeating", s.count(ch), "times")
 s = s.replace(ch, '', 1):
 '''
'''
2)
r is repeating 2 times
index = [1,4]
g is repeating 2 times
index = [3,10]
m is repeating 2 times
index =[6,7]
'''

s = input()

checked = []

for ch in s:
    if ch not in checked:
        checked.append(ch)

        if s.count(ch) > 1:
            print(ch, "is repeating", s.count(ch), "times")

            index = []
            for i in range(len(s)):
                if s[i] == ch:
                    index.append(i)

            print("index =", index)

'''
Sequences -->Strings,Lists,Tuples,Set,Frozenset
Mapping -> Dictionary

#Sets --> A set unique Collection of objects,Unordered,Mutable,Hashing,Unindexed,Unique,Heterogenous
#set(),{}
#a = {} its an empty dictionary
a = set()
print(type(a))
stud_ids = {123,345,234,567,234}
print(stud_ids)
print(type(stud_ids))
print(len(stud_ids))
#print(stud_ids[2]) #TypeError

print(234 in stud_ids)
#print(stud_ids *2)
#print(stud_ids + stud_ids)#Two sets cannot be Merged


data = {12,3,4,5,[12,3,4],'keerthi'}
print(data) #No lists inside a Set (hashing technique) lists are mutable

data = {12,3,4,5,(12,3,4),'keerthi'}
print(data)
print(len(data))
for i in data:
    print(i)
'''
#Methods on sets -->add(),update(),remove(),discard(),pop()
names = {'sai','chinnu','lasya','codegnan'}
print(len(names))
#add() will insert an elements into the set (it can be anywhere but only unique
names.add('python')
print(names)
#names.add('saketh','poll')
#print(names)
names.add(('poll','police'))
print(names)
da_names={'mani','akash','sai','sonu'}
print(da_names)
#udate() we can update multiple elements(set)

names.update(da_names)
print(names)
print(da_names)
print(len(da_names))
da_names.update(names)
print(len(names))
print(len(da_names))

'''
#remove(),discard(),pop(),clear()
da_names.remove('sai')
print(da_names)
#da_names.remove('sai') #keyError
#discard() will remove an element if its present else it ignores
da_names.discard('codegnan')


da_names.pop()
print(da_names)
print(da_names.pop()) # removes and returns an arbritrary elements
print(da_names)
da_names.clear()
print(da_names)
da_names.add('Saira')
print(da_names)
da_names.update(['sai','akash'])
print(da_names)


#copy() #creates a shallow copy of set (independent of each other)
d = da_names.copy()
print(d)
d.update({'python','codegnan'})
print(d)
print(da_names)

'''
#mathematical operations -->union(),intersection(),difference(),symmetric_d:
#issubset(),issuperset(),isdisjoint()
da_23 = {12,23,34,45,23,36}
da_24 = {34,46,47,23}
#event = da_23.union(da_24)
'''event = da_23 | da_24
print(event)
print(len(event))
#common = da_23.intersection(da_24)
common = da_23 & da_24 #& intersection()
print(common)
#print(len(common))
common = da_23.intersection_update(da_24)
print(common) # it returns None
print(da_23) # common elements are finally stored

print(da_23)
print(da_24)
#difference() removes common elements and prints rmng elements from first sequences
#diff = da_23.difference(da_24)
#print(diff)
#f = da_23 - da_24
#print(f)
#symmetric_difference() -->removes common and prints all  rmng
#elements from two sets
symm = da_23.symmetric_difference(da_24)
#print(symm)
h = da_23 ^ da_24
#print(h)

#issubset() -->checks for all elements to be present in other set
da_24.remove(46)
da_24.remove(47)

print(da_24.issubset(da_23))
print(da_23.issuperset(da_24))

#isdisjoint() returns false for sets having common elements
print(da_23.isdisjoint(da_24))
'''

#Length of unique student ids in a class,where user can enter first input
#he should be giving number of student_ids,he will enter student_ids

n = int(input())
student_ids = input().split()
#print(student_ids)
result = set(student_ids)
print(result)








































































