class InvalidNameError(Exception):
    def __init__(self, message="Name must be a string and should not contain numbers"):
        self.message = message
        super().__init__(self.message)
