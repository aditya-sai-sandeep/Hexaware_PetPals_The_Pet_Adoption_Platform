class InsufficientFundsException(Exception):
    def __init__(self, message="Insufficient funds for donation (amount should be at least 100)"):
        self.message = message
        super().__init__(self.message)
