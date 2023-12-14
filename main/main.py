from dao.ItemDonation import *
from entity.cat import Cat
from entity.dog import Dog
from entity.pet import Pet
from exception.AdoptionException import AdoptionException
from exception.FileHandlingException import FileHandlingException
from exception.InvalidNameError import *
from exception.InvalidAgeError import *
from dao.petshelter import *
from dao.CashDonation import *
from dao.Adoptionevent import *
from exception.NullReferenceException import *
from datetime import datetime

try:
    pet1 = Pet("python", 99, 'Animal')
    pet2 = Pet("java", 98, "Animal")
    dog1 = Dog("snoopy", 3, "Dog", "Bull Dog")
    dog2 = Dog("harper", 4, "Dog", "Golden")
    cat1 = Cat("misty", 3, "Cat", "orange")
    cat2 = Cat("sammy", 1, "Cat", "brown")
    petshelter1 = PetShelter()
except InvalidNameError as e:
    print(e)
except InvalidAgeError as e:
    print(e)
except Exception as e:
    print(e)

status = True
Once = True
try:
    petshelter1 = PetShelter()
    cashdonation1 = CashDonation()
    itemdonation1 = ItemDonation()
    adoptionevent1 = AdoptionEvent()
    while Once:
        petshelter1.create_table()
        cashdonation1.createTable()
        adoptionevent1.create_event()
        adoptionevent1.create_participants()
        adoptionevent1.create_adoption()
        itemdonation1.createTable()
        Once = False

    while status:

        print("Below are the list of applications")
        print("\n1.addCustomer\t2.list available pets\n3.Delete Pet\t"
              "4.Record Amount Donation\n5.View Amount DonationData\t6.Record Toys Donation\n7.view "
              "Toys Donation data\t8.Register Participant for event"
              "\n9.Get Participants Details \t10.Add New Host Event\n11.Get Host 7Event Details\t12.See Adoption Data "
              "\n13.Proceed for Adoption\t14.Exit")
        choice = int(input("enter above choices"))

        if choice == 1:
            print("create object to add into Pets table")
            print("1.For Pets\n2.For Dogs\n3.For Cat")
            choice = int(input("enter choice"))
            if choice == 1:
                name = input("enter name")
                age = int(input("enter age"))
                breed = input("enter breeed")
                obj1 = Pet(name, age, breed)
                petshelter1.AddPet(obj1)
            elif choice == 2:
                name = input("enter name")
                age = int(input("enter age"))
                breed = input("enter breeed")
                dog_breed = input("enter sub breed")
                obj1 = Dog(name, age, breed, dog_breed)
                petshelter1.AddPet(obj1)
            else:
                name = input("enter name")
                age = int(input("enter age"))
                breed = input("enter breed")
                color = input("enter color")
                obj1 = Cat(name, age, breed, color)
                petshelter1.AddPet(obj1)
        elif choice == 2:
            petshelter1.ListAvailablePets()
        elif choice == 3:
            id = int(input("enter ID"))
            petshelter1.RemovePet(id)
        elif choice == 4:
            name = input("enter name")
            amount = int(input("enter amount"))
            date = input("enter date")
            cashdonation1 = CashDonation(name, amount, date)
            cashdonation1.RecordDonation()
        elif choice == 5:
            cashdonation1.ViewAmountDonationData()
        elif choice == 6:
            name = input("enter name")
            amount = int(input("enter amount"))
            item = input("enter item")
            itemdonation1 = ItemDonation(name, amount, item)
            itemdonation1.RecordDonation()
        elif choice == 7:
            itemdonation1.ViewItemDonationData()
        elif choice == 8:
            adoptionevent1.RegisterParticipant()
        elif choice == 9:
            adoptionevent1.GetParticipants()
        elif choice == 10:
            adoptionevent1.HostEvent()
        elif choice == 11:
            adoptionevent1.GetEvent()
        elif choice ==12:
            adoptionevent1.ViewAdoption()
        elif choice == 13:
            adoptionevent1.Adopt()
        else:

            status = False
except InvalidNameError as e:
    print(e)
except InvalidAgeError as e:
    print(e)
except InvalidAmountError as e:
    print(e)
except InsufficientFundsException as e:
    print(e)
except DuplicateObjError as e:
    print(e)
except NullReferenceException as e:
    print(e)
except AdoptionException as e:
    print(e)
except FileHandlingException as e:
    print(e)
except Exception as e:
    print(e)
