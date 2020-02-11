
class Animal:
    def __init__(self, name, sounds,eat):
        self.name = name
        self.sounds = sounds
        
class Dog(Animal):
    def DogName(self):
        return('Rax')     
    def sound(self):
        return("barks") 
    def eats(self):
        return("eat")

class Cat(Animal):
    def CatName(self):
        return('stormy') 
    def sound(self):
        return("meow")  
    def eats(self):
        return("eat")

d = Dog(' ',' ',' ')
c = Cat(' ',' ',' ')
print(d.DogName() + " " + d.sound()+ " " + " and" + " " + d.eats())
print(c.CatName() + " " + c.sound()+ " " + "and" +  " " +c.eats())

class Home:
    def __init__(self):
        self.o1 = Dog('','','')
        self.o2 = Cat('','','')

    def adoptPet(self):
        print('cat','dog')

    def MakeAllSounds(self):
        return self.o1.bark()

Rax = Home('bark',' meow','eat')
Rax.bark()        

  