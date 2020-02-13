from animal import Animal
from cat import Cat
from dog import Dog

class Home:
    def __init__(self,pets = []):
        self.pets = pets

    def adopt_pets(self,pet):
        for each in self.pets:
            if each == pet:
                raise Exception ("cant adopt the same pet twice")
        self.pets.append(pet)

if __name__ == "__main__":
    home = Home()
    dog_1 = Dog("Rax", "barks")
    cat_2 = Cat("Stormy", "meows")
    home.adopt_pets(dog_1)
    home.adopt_pets(cat_2)
    #home.adopt_pets(cat_1)
    print("current pets")
    print(home.pets)
