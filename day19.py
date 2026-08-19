'''
Functions -->Variable length arguments (*args)
          -->Keyword Variable length arguments (**kwargs)

Variable length arguments -->The number of positional arguments are not limit
we can pass any number of arguments,but we need to use the * representation,dat is stored in tuple.


def sample(*args):
    """Simple demo for *args"""
    print(args)
    print(type(args))
sample()
sample(1,3,5,6)
sample('codegnan','saketh',23)
details = [24,45,35,65]
sample(details)#passing a collection
sample(*details)#unpacking values from collection

#* is used for unpacking the values into a collection
a,b,c = 13,4,'da'
print(a,b,c)
#a,*b,c = 'python','codegnan',23,45,9.7,'data'
#a,b,*c = 'python','codegnan',23,45,9.7,'data'
a,b,*c = 34,'codegnan'
print(a)
print(b)
print(c)
c.extend([23,45,6,7])
print(c)

#Task --> We wanted to caculate the sum of given objects using Function
def add(*a):
    """Sum of given objects"""
    print(a)
    print(type(a))
    #take output variable as result
    result = 0
    for i in a:
        #if  type(i)==int or type(i)==float:
        if type(i) in (int,float,complex):
             #print(i)
             result = result + i
    return result
#print(add())
#print(add(12,3,4,5))
#print(add(1,2,3,4,5))
#print(add(3,4,5,'poll','dear',45,4.5))
#print(add(23,4,5.5,2+4j,56,'code',23))
b = list(map(int,input("Enter the values").split(',')))
print(add(*b)) #* is used to unpack the values from collection 
#print(b)
print(*b) # it returns each value side by side
for i in b:
    print(i,end=' ')#same as here
,,,
#keyword variable length arguments -->we can pass any number of keyword arguments we use ** representation,data is stored in dictionary

def details(**kwargs):
    """Usage of **kwargs demo"""
    print(kwargs)
    print(type(kwargs))
details()#returns empty dictionary
#details(2,3,4,6,)#raises TypeError
details(name="codegnan",place="Hyd",batch="da")
details(ids=12345,age = 47)
batch = {'number':'da23','place':'hyd'}
details(**batch)
'''
#Now let us include both of them into a function
def sample(*a,**b):
    """Usage of both variable length and keyword variable length args"""
    result = 0
    for i in a :
        if type(i) in(int,float,complex):
            result = result + i
    #print(result)
    #return result       
    for key,value in b.items():
        print(f'key is {key}')
        print(f'Value is {value}')
    return result    
sample(2,4,5,'police','codegnan',3.5,
       name = "codegnan",
       place = "hyd",
       batch = "da23")

#sanple(name="codegnan",23,ids=2345)#positional args follows keyword args
        
    



















