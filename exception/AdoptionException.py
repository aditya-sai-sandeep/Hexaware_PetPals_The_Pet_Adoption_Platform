class AdoptionException(Exception):
    def __init__(self, message="This pet is already adopted"):
        self.message = message
        super().__init__(self.message)
