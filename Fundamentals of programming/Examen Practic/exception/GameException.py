class GameException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class GameOver(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message