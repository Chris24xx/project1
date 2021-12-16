class NoNegativeException(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectInfo(Exception):
    def __init__(self,message):
        self.message = message
