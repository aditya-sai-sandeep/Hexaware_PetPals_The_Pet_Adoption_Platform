from exception.InvalidNameError import *
from exception.InvalidAgeError import *


class Pet:
    def __init__(self, name, age, breed):
        if not isinstance(name, str):
            raise InvalidNameError()
        for i in name:
            if not i.isalpha() and not i.isspace():
                raise InvalidNameError()
        if not isinstance(age, int) or age < 0:
            raise InvalidAgeError("Age must be a non-negative integer")
        if not isinstance(breed, str):
            raise InvalidNameError("Breed must be a string and should not contain numbers")
        for i in breed:
            if not i.isalpha() and not i.isspace():
                raise InvalidNameError("Breed must be a string and should not contain numbers")
        self.name = name
        self.age = age
        self.breed = breed

    def get_name(self):
        return self.name

    def set_name(self, name):
        if not isinstance(name, str):
            raise InvalidNameError()
        for i in name:
            if not i.isalpha() and not i.isspace():
                raise InvalidNameError()
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        if not isinstance(age, int) or age < 0:
            raise InvalidAgeError("Age must be a non-negative integer")
        self.age = age

    def get_breed(self):
        return self.breed

    def set_breed(self, breed):
        if not isinstance(breed, str):
            raise InvalidNameError("Breed must be a string and should not contain numbers")
        for i in breed:
            if not i.isalpha() and not i.isspace():
                raise InvalidNameError("Breed must be a string and should not contain numbers")
        self.breed = breed

    def update_by_name(self, new_age=None, new_breed=None):
        if new_age is not None:
            if not isinstance(new_age, int) or new_age < 0:
                raise InvalidAgeError("Age must be a non-negative integer")
            self.age = new_age

        if new_breed is not None:
            if not isinstance(new_breed, str):
                raise InvalidNameError("Breed must be a string and should not contain numbers")
            for i in new_breed:
                if not i.isalpha() and not i.isspace():
                    raise InvalidNameError("Breed must be a string and should not contain numbers")
            self.breed = new_breed

    def __str__(self):
        return f"{self.name}, {self.age} years old, {self.breed}"


try:

    pet1 = Pet("snoopy", 3, 'Dog')
except InvalidNameError as e:
    print(e)
except InvalidAgeError as e:
    print(e)
except Exception as e:
    print(e)
