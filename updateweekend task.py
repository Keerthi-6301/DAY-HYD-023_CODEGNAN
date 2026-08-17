
'''#day16Task:#Length of unique student ids in a class,where user can enter first input
#he should be giving number of student_ids,he will enter student_ids
#n = int(input())
#student_ids = input().split()
#print(student_ids)
#result = set(student_ids)
#print(result)

n = int(input("Enter number of student IDs: "))
student_ids = input("Enter student IDs: ").split()
result = set(student_ids)
print("Unique student IDs:", result)
print("Length:", len(result))


#TASK 1: Student marks manager
#Scenario: A teacher wants to bulid and update a simple list of student marks.
#Task : write  a program that accepts marks,adds more values,removes selected values,aand displays the final list
#Starting data:use the following list
#numbers = [29,10,30,20,40,20]
marks = []

for i in range(3):
    m = int(input("Enter  the mark: "))
    marks.append(m)

print("Original list:", marks)

marks.insert(0, 90)
marks.extend([65, 75])

if 65 in marks:
    marks.remove(65)

removed = marks.pop()

print("Removed mark:", removed)
print("Final list:", marks)
print("Length:", len(marks))

#Task 2: Number List Analyser
#Scenario : yoy have a list containing unsorted and repeated numbers
#starting data: use the following list

numbers=[20,10,30,20,40,20]
numbers.sort()
print("Sorted list:", numbers)
print("Ascending values:")
for i in numbers:
    print(i)
numbers.reverse()
print("Reversed list:", numbers)
print("Descending values:")
for i in numbers:
    print(i)
num=int(input("Enter the number to search: "))
if num in numbers:
    print("Count:", numbers.count(num))
    print("First Index:", numbers.index(num))
else:
    print("Number not found")
print("Smallest number:", min(numbers))
print("Largest number:", max(numbers))
print("Sum:", sum(numbers))

#Task 3: Even and Odd Number Separator
#Scenario : A program must separate a mixed list into even and odd numbers
#Starting data:use the following list
#numbers =[10,15,20,25,30,35]

numbers = [10, 15, 20, 25, 30, 35]

even = []
odd = []
for n in numbers:
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
print("Even:", even)
print("Odd:", odd)
print("First 3:", numbers[:3])
print("Last 3:", numbers[-3:])
backup = numbers.copy()
numbers.clear()
print("Original list:", numbers)
print("Backup:", backup)

#Task 4:Unique Name Manger
#Scenario:A class list contains repeated student names and needs to be cleaned
#Starting data:Use the following list..
#names = ["Asha","Rahul","Asha","John",,"Rahul"]

names = ['Asha', 'Rahul', 'Asha', 'John', 'Rahul']

a = set(names)
print(a)

a.add('keerthi')
print('Added:', a)

a.update(['baji', 'nithya'])
print('Updated:', a)

if 'John' in names:
    a.remove('John')
    print('Removed:', a)

a.discard('chinnu')
print('Discarded:', a)

for i in names:
    print(i)

    
#Task 5: Course student comparision
#Scenario:A training center wants to compare the students enrolled in python and java courses.
#Starting data:create the following sets..
#python_students ={"Asha","Rahul","John","Meera"}
python_students={'Asha','Rahul','John','Meera'}
da_students={'Rahul','Meera','Arun'}
a=python_students.union(da_students)
b=python_students.intersection(da_students)
c=python_students.difference(da_students)
d=python_students.symmetric_difference(da_students)
print('All Students:')
for i in a:
    print(i)
print('Students have both courses:')
for j in b:
    print(j)
print('Only Python:') 
for k in c:
    print(k)
print('Only one course:')
for m in d:
    print(m)
    
print("\nDA is subset of Python:", da_students.issubset(python_students))
if da_students.issubset(python_students):
    print("All DA students are also Python students")
else:
    print("All DA students are not Python students")

print("Python is superset of DA:", python_students.issuperset(da_students))
if python_students.issuperset(da_students):
    print("Python contains all DA students")
else:
    print("Python does not contain all DA students")

print("Both sets are disjoint:", python_students.isdisjoint(da_students))
if python_students.isdisjoint(da_students):
    print("There are no common students")
else:
    print("There are common students in both courses")

'''
