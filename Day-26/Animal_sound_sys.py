#Animal Sound System 🐶🐱


class Animals:
    
    def sound(self):
        print("Animal makes a sound")
        
class Dog(Animals):
         
     def sound(self):
      print("DOG SAYS: BARK BARK")  
            
class Cat(Animals):
    def sound(self):
        print("CAT SAYS: MEOW MEOW")


class Cow(Animals):
    def sound(self):
        print("COW SAYS: MOO MOO")

dog1  = Dog()
cat1 = Cat()
cow1 = Cow() 
      
      
dog1.sound()
cat1.sound()
cow1.sound()      
