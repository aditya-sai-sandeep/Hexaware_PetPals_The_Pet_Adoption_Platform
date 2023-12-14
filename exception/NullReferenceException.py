class NullReferenceException(Exception):
    def __init__(self, message="It is missing some details"):
        self.message = message
        super().__init__(self.message)
