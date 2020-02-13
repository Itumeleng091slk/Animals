from test import Animal

class Cat(Animal):
   def __init__(self, name, sounds):
        super().__init__(name,sounds)

   def food(self):
        print(self.name + " eats")  

   def sound(self):
        print(self.sounds,"meows")

cat_1 = Cat("Stormy","Cat")
cat_1.food()
cat_1.sound()
