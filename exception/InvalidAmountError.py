class InvalidAmountError(Exception):
    def __init__(self, message="Must be a positive decimal."):
        self.message = message
        super().__init__(self.message)
