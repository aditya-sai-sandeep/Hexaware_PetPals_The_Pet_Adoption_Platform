from entity.pet import Pet
from exception.InvalidNameError import *


class Dog(Pet):
    def __init__(self, name, age, breed, dog_breed):
        super().__init__(name, age, breed)
        if not isinstance(dog_breed, str):
            raise InvalidNameError("Breed should be a string and should not contain numbers")
        for i in dog_breed:
            if not i.isalpha() and not i.isspace():
                raise InvalidNameError("Breed must be a string and should not contain numbers")
        self.dog_breed = dog_breed

    def get_dog_breed(self):
        return self.dog_breed

    def set_dog_breed(self, dog_breed):
        if not isinstance(dog_breed, str):
            raise InvalidNameError("Breed should be a string and should not contain numbers")
        for i in dog_breed:
            if not i.isalpha() and not i.isspace():
                raise InvalidNameError("Breed must be a string and should not contain numbers")
        self.dog_breed = dog_breed

    def __str__(self):
        return f"{self.name}, {self.age} years old, belongs to {self.breed}, {self.dog_breed}."


try:

    dog1 = Dog("snoopy", 3, "Dog", "Bull Dog")
    dog2 = Dog("harper", 4, "Dog", "Golden")
except InvalidNameError as e:
    print(e)
except Exception as e:
    print(e)
