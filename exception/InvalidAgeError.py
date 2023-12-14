class InvalidAgeError(Exception):
    def __init__(self, message="Invalid age for a dog"):
        self.message = message
        super().__init__(self.message)
