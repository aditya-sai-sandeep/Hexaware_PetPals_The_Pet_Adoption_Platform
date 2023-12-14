class DuplicateObjError(Exception):
    def __init__(self, message="Duplicate pet object"):
        self.message = message
        super().__init__(self.message)
