from entity.donation import Donation
import mysql.connector as sql

from exception.InsufficientFundsException import InsufficientFundsException
from exception.InvalidAmountError import InvalidAmountError
from exception.InvalidNameError import InvalidNameError
from util.DBConnUtil import dbConnection



class CashDonation(Donation, dbConnection):

    def __init__(self, donor_name=None, amount=None, donation_date=None):
        if donor_name!=None and amount!=None and donation_date!=None:
            if not isinstance(donor_name, str):
                raise InvalidNameError()
            for i in donor_name:
                if not i.isalpha() and not i.isspace():
                    raise InvalidNameError()
            if not isinstance(amount, (int, float)) or amount <= 0:
                raise InvalidAmountError()
            elif amount < 100:
                raise InsufficientFundsException()
            self.donor_name = donor_name
            self.amount = amount
            self.donation_date = donation_date
            self.result_list = []

    def createTable(self):
        try:
            self.open()
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS CashDonation (
                id INT PRIMARY KEY AUTO_INCREMENT,
                DonorName VARCHAR(255) NOT NULL,
                Amount DECIMAL(10, 2) NOT NULL
            );
            '''
            self.stmt.execute(create_table_query)
            print("CashDonation table is created.")
            self.close()
        except Exception as e:
            print(f"Error creating CashDonation table: {e}")

    def RecordDonation(self):
        try:
            self.open()
            insert_query = "INSERT INTO CashDonation (DonorName, Amount) VALUES (%s, %s)"
            self.stmt.execute(insert_query, (self.donor_name, self.amount))
            self.conn.commit()
            print("Cash donation recorded successfully.")
            self.close()
        except Exception as e:
            print(f"Error recording cash donation: {e}")

    def ViewAmountDonationData(self):
        try:
            self.open()
            select_query = "SELECT * FROM CashDonation"
            self.stmt.execute(select_query)
            records = self.stmt.fetchall()
            self.result_list = []
            for record in records:
                print(record)
                self.result_list.append({
                    "id": record[0],
                    "donor_name": record[1],
                    "amount": record[2]
                })
            self.close()
            return self.result_list
        except Exception as e:
            print(f"Error selecting from CashDonation table: {e}")
