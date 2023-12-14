from entity.pet import Pet
from exception.InvalidNameError import *


class Cat(Pet):
    def __init__(self, name, age, breed, cat_color):
        super().__init__(name, age, breed)
        if not isinstance(cat_color, str):
            raise InvalidNameError("Cat color must be a string")
        for i in cat_color:
            if not i.isalpha() and not i.isspace():
                raise InvalidNameError("Color must be a string and should not contain numbers")
        self.cat_color = cat_color

    def set_cat_color(self, cat_color):
        if not isinstance(cat_color, str):
            raise InvalidNameError("Cat color must be a string")
        for i in cat_color:
            if not i.isalpha() and not i.isspace():
                raise InvalidNameError("Color must be a string and should not contain numbers")
        self.cat_color = cat_color

    def get_cat_color(self):
        return self.cat_color

    def __str__(self):
        return f"{self.name}, {self.age} years old, belongs to {self.breed}, is of {self.cat_color} in color"


try:

    cat1 = Cat("misty", 3, "Cat", "orange")
    cat2 = Cat("sammy", 1, "Cat", "brown")
except InvalidNameError as e:
    print(e)
except Exception as e:
    print(e)
