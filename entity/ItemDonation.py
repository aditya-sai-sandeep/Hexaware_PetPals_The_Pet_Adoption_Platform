from entity.donation import Donation


class ItemDonation(Donation):
    def __init__(self, donor_name, amount, item_type):
        super().__init__(donor_name, amount)
        self.item_type = item_type

    def record_donation(self):
        # Implement item donation recording logic here
        print(f"Item donation of {self.item_type} recorded.")


item_donation = ItemDonation("Aditya", 50.0, "Toys")
item_donation.record_donation()