import mysql.connector as sql

from entity.IAdoptable import IAdoptable
from exception.InvalidNameError import InvalidNameError
from util.DBConnUtil import dbConnection
from dao.petshelter import *
class AdoptionEvent(dbConnection,IAdoptable):



    def create_event(self):
        try:
            self.open()
            create_event_query = '''
            CREATE TABLE IF NOT EXISTS Event (
                ID INT PRIMARY KEY AUTO_INCREMENT,
                Details VARCHAR(255) NOT NULL
            );
            '''
            self.stmt.execute(create_event_query)
            print("Event table is created.")
            self.close()
        except Exception as e:
            print(f"Error creating Event table: {e}")

    def create_participants(self):
        try:
            self.open()
            create_participants_query = '''
            CREATE TABLE IF NOT EXISTS Participants (
                ID INT PRIMARY KEY AUTO_INCREMENT,
                Name VARCHAR(255) NOT NULL
            );
            '''
            self.stmt.execute(create_participants_query)
            print("Participants table is created.")
            self.close()
        except Exception as e:
            print(f"Error creating Participants table: {e}")

    def create_adoption(self):
        try:
            self.open()
            create_participants_query = '''
            CREATE TABLE IF NOT EXISTS Adopt (
                petname VARCHAR(50),
                petage INTEGER,
                petbreed VARCHAR(50),
                name VARCHAR(50)
            );
            '''
            self.stmt.execute(create_participants_query)
            print("Adopt table is created.")
            self.close()
        except Exception as e:
            print(f"Error creating Participants table: {e}")

    def RegisterParticipant(self):
        try:
            participant_name = input("Enter participant name: ")

            if not isinstance(participant_name, str):
                raise InvalidNameError()
            for i in participant_name:
                if not i.isalpha() and not i.isspace():
                    raise InvalidNameError()

            self.open()
            insert_query = "INSERT INTO Participants (Name) VALUES (%s)"
            self.stmt.execute(insert_query, (participant_name,))
            self.conn.commit()
            print(f"Participant '{participant_name}' added successfully.")
            self.close()
        except Exception as e:
            print(f"Error adding participant: {e}")

    def GetParticipants(self):
        try:
            self.open()
            select_query = "SELECT * FROM Participants"
            self.stmt.execute(select_query)
            records = self.stmt.fetchall()
            for i in records:
                print(i)
            self.close()
        except Exception as e:
            print(f"Error getting participants: {e}")

    def HostEvent(self):
        try:
            event_details = input("Enter event details: ")

            # Add the event to the database
            self.open()
            insert_query = "INSERT INTO Event (Details) VALUES (%s)"
            self.stmt.execute(insert_query, (event_details,))
            self.conn.commit()
            print("Event hosted successfully.")
            self.close()
        except Exception as e:
            print(f"Error hosting event: {e}")

    def GetEvent(self):
        try:
            self.open()
            select_query = "SELECT * FROM Event"
            self.stmt.execute(select_query)
            records = self.stmt.fetchall()
            for i in records:
                print(i)
            self.close()
        except Exception as e:
            print(f"Error getting events: {e}")

    def ViewAdoption(self):
        try:
            self.open()
            view_adoption_query = "SELECT * FROM Adopt;"
            self.stmt.execute(view_adoption_query)
            result = self.stmt.fetchall()
            if result:
                print("Adoption table data:")
                for row in result:
                    print(row)
            else:
                print("No data found in Adoption table.")

            self.close()
        except Exception as e:
            print(f"Error viewing Adoption table: {e}")

    def InsertAdoption(self, petname, petage, petbreed, name):
        try:
            self.open()
            insert_adoption_query = "INSERT INTO Adopt (petname, petage, petbreed, name) VALUES (%s, %s, %s, %s);"
            self.stmt.execute(insert_adoption_query, (petname, petage, petbreed, name))
            print("Adoption data inserted successfully.")
            self.conn.commit()
            self.close()
        except Exception as e:
            print(f"Error inserting data into Adopt table: {e}")

    def Adopt(self):
        try:
            self.open()
            select_query = "SELECT * FROM Pets"
            self.stmt.execute(select_query)
            records = self.stmt.fetchall()
            for i in records:
                print(i)
        except sql.Error as e:
            print(f"Error listing available pets: {e}")
        self.GetParticipants()

        try:
            id = int(input("enter petID"))
            self.open()
            select_query = "SELECT * FROM Pets where id=%s"
            self.stmt.execute(select_query,(id,))
            records = self.stmt.fetchall()[0]
            print(records)
            petID = records[0]
            petname = records[1]
            petage = records[2]
            petbreeed = records[3]
            self.close()
            nameid = int(input("enter participantID"))
            self.open()
            select_query = "SELECT * FROM Participants where ID=%s"
            self.stmt.execute(select_query,(nameid,))
            records = self.stmt.fetchall()[0]
            name = records[1]
            print(name)
            self.close()
            self.InsertAdoption(petname, petage, petbreeed, name)
            print(f'{name} adopted {petname} successfully')
            delete_query = f"DELETE FROM Pets WHERE id = {petID}"
            self.open()
            self.stmt.execute(delete_query)
            self.conn.commit()
            print("Pet is successfully removed from Shelter!!")

        except Exception as e:
            print(f"Error getting participants: {e}")






