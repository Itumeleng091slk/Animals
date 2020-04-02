class Animal:
    def __init__(self, name, sounds):
        self.name = name
        self.sounds = sounds
        

    def food(self):
        return("{0} eats".format(self.name))

    def sound(self):
        return("{0} barks".format(self.sounds))
        
dog = Animal("Rax","Dog")
cat =Animal("Stormy","cat")

dog.food() #Comment these two functions in Animal class so that the function in dog.py executes the specified output.
dog.sound()
