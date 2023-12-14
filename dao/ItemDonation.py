from entity.donation import Donation
from exception.InvalidAmountError import InvalidAmountError
from exception.InvalidNameError import InvalidNameError
from util.DBConnUtil import dbConnection


class ItemDonation(Donation,dbConnection):
    donation_data = []

    def __init__(self, donor_name=None, amount=None, itemtype=None):
        if donor_name != None and amount != None and itemtype != None:
            if not isinstance(donor_name, str):
                raise InvalidNameError()
            for i in donor_name:
                if not i.isalpha() and not i.isspace():
                    raise InvalidNameError()
            if not isinstance(amount, (int, float)) or amount <= 100:
                raise InvalidAmountError()
            self.donor_name = donor_name
            self.amount = amount
            self.itemtype = itemtype

    def createTable(self):
        try:
            self.open()
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS ItemDonation (
                id INT PRIMARY KEY AUTO_INCREMENT,
                donor_name VARCHAR(255) NOT NULL,
                amount DECIMAL(10, 2) NOT NULL,
                itemtype VARCHAR(50) NOT NULL
            );
            '''
            self.stmt.execute(create_table_query)
            print("ItemDonation table is created.")
            self.close()
        except Exception as e:
            print(f"Error creating ItemDonation table: {e}")

    def ViewItemDonationData(self):
        try:
            self.open()
            select_query = "SELECT * FROM ItemDonation;"
            self.stmt.execute(select_query)
            result = self.stmt.fetchall()

            if result:
                print("ItemDonation table data:")
                for row in result:
                    print(f"ID: {row[0]}, Donor Name: {row[1]}, Amount: {row[2]}, ItemType: {row[3]}")
            else:
                print("ItemDonation table is empty.")

            self.close()
        except Exception as e:
            print(f"Error viewing data from ItemDonation table: {e}")

    def RecordDonation(self):
        try:
            self.open()
            insert_query = '''
            INSERT INTO ItemDonation (donor_name, amount, itemtype) 
            VALUES (%s, %s, %s);
            '''
            values = (self.donor_name, self.amount, self.itemtype)
            self.stmt.execute(insert_query, values)
            self.conn.commit()
            print("Record added to ItemDonation table.")
            self.close()
        except Exception as e:
            print(f"Error adding record to ItemDonation table: {e}")
