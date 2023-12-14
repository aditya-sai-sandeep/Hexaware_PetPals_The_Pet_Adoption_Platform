from entity.donation import Donation
from datetime import datetime


class CashDonation(Donation):
    def __init__(self, donor_name, amount, donation_date):
        super().__init__(donor_name, amount)
        self.donation_date = donation_date

    def record_donation(self):
        # Implement cash donation recording logic here
        print(f"Cash donation of {self.amount} recorded on {self.donation_date}.")


cash_donation = CashDonation("Aditya", 100.0, datetime.now())
cash_donation.record_donation()
