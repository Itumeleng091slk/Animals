from animal import Animal

class Dog(Animal):
    def __init__(self, name, sounds):
        super().__init__(name,sounds)

    def food(self):
        return(self.name + " eats")  

    def sound(self):
        return(self.sounds,"barks")

dog_1 = Dog("Rax","Dog")
dog_1.food()
dog_1.sound()
