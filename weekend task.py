#day16Task:#Length of unique student ids in a class,where user can enter first input
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

'''
#TASK 1: Student marks manager
#Scenario: A teacher wants to bulid and update a simple list of student marks.
#Task : write  a program that accepts marks,adds more values,removes selected values,aand displays the final list
#Starting data:use the following list
#numbers = [29,10,30,20,40,20]
marks = []

for i in range(3):
    m = int(input("Enter mark: "))
    marks.append(m)

print("Original list:", marks)

marks.insert(0, 90)
marks.extend([75, 85])

if 75 in marks:
    marks.remove(75)

removed = marks.pop()

print("Removed mark:", removed)
print("Final list:", marks)
print("Length:", len(marks))

#Task 2: Number List Analyser
#Scenario : yoy have a list containing unsorted and repeated numbers
#starting data: use the following list

numbers = [20, 10, 30, 20, 40, 20]
numbers.sort()
print("Ascending:", numbers)
numbers.reverse()
print("Descending:", numbers)
n = int(input("Enter number to search: "))
if n in numbers:
    print("Count:", numbers.count(n))
    print("First index:", numbers.index(n))
else:
    print("Number not found")

print("Smallest:", min(numbers))
print("Largest:", max(numbers))
print("Total:", sum(numbers))

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
print("Original:", numbers)
print("Backup:", backup)

#Task 4:Unique Name Manger
#Scenario:A class list contains repeated student names and needs to be cleaned
#Starting data:Use the following list..
#names = ["Asha","Rahul","Asha","John",,"Rahul"]

names = ["Asha", "Rahul", "Asha", "John", "Rahul"]
names = set(names)
names.add("keeru")
names.update(["gnana", "Priya"])
if "John" in names:
    names.remove("John")
names.discard("lasya")
for name in names:
    print(name)
    
#Task 5: Course student comparision
#Scenario:A training center wants to compare the students enrolled in python and java courses.
#Starting data:create the following sets..
#python_students ={"Asha","Rahul","John","Meera"}
da_students={"Rahul","Meera","Arun"}
python_students = {"Asha", "Rahul", "John", "Meera"}
da_students = {"Rahul", "Meera", "Arun"}
print("All students:", python_students.union(da_students))
print("Both courses:", python_students.intersection(da_students))
print("Only Python:", python_students.difference(da_students))
print("Only one course:", python_students.symmetric_difference(da_students))
print("DA subset of Python:", da_students.issubset(python_students))
print("Python superset of DA:", python_students.issuperset(da_students))
print("Disjoint:", python_students.isdisjoint(da_students))
print("\nStudents in both:")
for name in python_students.intersection(da_students):
    print(name)




