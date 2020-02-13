from animal import Animal

class Dog(Animal):
    def __init__(self, name, sounds):
        super().__init__(name,sounds)

    def food(self):
        print(self.name + " eats")  

    def sound(self):
        print(self.sounds,"barks")

dog_1 = Dog("Rax","Dog")
dog_1.food()
dog_1.sound()
