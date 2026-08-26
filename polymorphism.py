'''
polymorphism --> It is also of one key feature of oop,
poly -->many
morph -->forms
Methods with same name can take different parameters(argument)
-->Method Overloading (compile time polymorphism)
-->Method Overriding (Run-time)
-->Operator Overloading (+,*) (__add__,__str__)

Hotstar
->Free User -->can watch the movies with advertisements
-->Premium User -->can watch premium content without advertisements
-->VIP User -->live content,streming quality,premium content

#Method Overloading :

class Hotstar:
    """Understand polymorphism"""
    def watch():
        print(f'User logged into Hotstar...Opening home page')
    def watch(self,movie):
        self.movie = movie    
        print(f'User watching{self.movie}')
app = Hotstar()
app.watch("Leo")
#app.watch() it returns error as watch() is overloaded 


#1)Method usage with default arguments
#2)Method usage with variable length arguments (*args)
#3)Method usage with type of arguments

class Hotstar:
    """Method usage with default arguments"""
    def watch(self,movie=None):
        if movie is None:
            print(f'User logged into Hotstar...checking')
        else:
            self.movie = movie
            print('User started watching {self.movie}')
app = Hotstar()
app.watch()
app.watch("Vikram")
                
class Hotstar:
    """Method usage with default arguments"""
    def add_watchlist(self,*movies):
        print(movies)
        for movie in movies:
            self.movie = movie
            print(f'User watching{self.movie}')

app = Hotstar()
app.add_watchlist()                               
app.add_watchlist("Leo,RRR,Shivam,Vikram")
#method overloading with type of arguments usage
#hostar -->one movie at a time
        -->multiple movies at a time 
#how we use different type of perameters
class Hotstar:
    """Method Overloading with type of arguments usage"""
    def watch(self,content):
        if isinstance(content,str):
            print(f'User watching {content}') 
        elif isinstance(content,list):
            print('Playing Playlist')
            print(content)
            for movie in content:
                print(movie)
app = Hotstar()
app.watch("Vikram")
app.watch(["Vikram", "Leo", "Master"])  

#method overriding -->it happens in the scenario ,where if child class is having method 
#name same as parent class thaths where override
#we can use super() or if we create different objects

class Freeuser:
    """Understanding method overriding"""
    def watch(self):
        print("User logged into Homepage....")
class PremiumUser(Freeuser):
    """Using Inheritance"""
    def watch(self,movie):
        self.movie = movie
        print(f'User watching {self.movie}')
obj = PremiumUser()
obj.watch("Vikram")
obj2 = Freeuser()
obj2.watch()  
#In the above usecase we can create different object to access same method but in real scenario what if similar to subscription plan
'''                          
class Freeuser:
    """Understanding method overriding"""
    def watch(self):
        print("User logged into Homepage....")
class PremiumUser(Freeuser):
    """Using Inheritance and super()"""
    def watch(self, movie):
        super().watch()   
        self.movie = movie
        print(f"User watching {self.movie}")


obj = PremiumUser()
obj.watch("loki")

