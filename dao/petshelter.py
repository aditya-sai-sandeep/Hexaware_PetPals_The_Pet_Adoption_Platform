from entity.pet import Pet
import mysql.connector as sql

from exception.DuplicateObjError import DuplicateObjError
from util.DBConnUtil import dbConnection

class PetShelter(dbConnection):
    available_pets = []

    def create_table(self):
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS Pets (
            id INT PRIMARY KEY AUTO_INCREMENT,
            Name VARCHAR(255) NOT NULL,
            Age INT,
            Breed VARCHAR(255) NOT NULL
        );
        '''
        self.open()
        self.stmt.execute(create_table_query)
        print("Table Pets is created.")
        self.close()

    def AddPet(self,pet):
        try:
            if not isinstance(pet, Pet):
                raise ValueError("Invalid pet type.")

            # Check if a pet with the same details already exists
            self.ListAvailablePets()
            for existing_pet in self.available_pets:
                print(existing_pet)
                if (
                        existing_pet["name"] == pet.name
                        and existing_pet["age"] == pet.age
                        and existing_pet["breed"] == pet.breed
                ):
                    raise DuplicateObjError()

            insert_query = "INSERT INTO Pets (Name, Age, Breed) VALUES (%s, %s, %s)"
            self.open()
            self.stmt.execute(insert_query, (pet.get_name(), pet.get_age(), pet.get_breed()))
            self.conn.commit()
            self.close()

            # Update available_pets list after a successful insert
            self.ListAvailablePets()

            print(f"{pet.get_name()} added to the list of available pets.")
        except sql.Error as e:
            print(f"Error adding pet: {e}")
        except DuplicateObjError as e:
            print("Duplicate pet object. Pet not added.")
        except ValueError as ve:
            print(f"Error: {ve}")

    def ListAvailablePets(self):
        try:
            self.open()
            select_query = "SELECT * FROM Pets"
            self.stmt.execute(select_query)
            records = self.stmt.fetchall()
            for i in records:
                self.available_pets.append({
                    "id": i[0],
                    "name": i[1],
                    "age": i[2],
                    "breed": i[3],
                    "adopt":False
                })
                print(i)
                self.close()
        except sql.Error as e:
            print(f"Error listing available pets: {e}")

    def get_pet_id(self, pet):
        self.ListAvailablePets()
        for record in self.available_pets:
            if record["name"] == pet.name and record["age"] == pet.age and record["breed"] == pet.breed:
                return record["id"]
        return None

    def RemovePet(self, petid):
        try:
            if isinstance(petid, int) or petid<0:
                if petid:
                    delete_query = f"DELETE FROM Pets WHERE id = {petid}"
                    self.open()
                    self.stmt.execute(delete_query)
                    self.conn.commit()
                    self.close()
                    self.ListAvailablePets()
                    print("deleted successfully!!")
                else:
                    print(f"not found in the list.")
            else:
                print("Invalid pet type.")
        except sql.Error as e:
            print(f"Error removing pet: {e}")
