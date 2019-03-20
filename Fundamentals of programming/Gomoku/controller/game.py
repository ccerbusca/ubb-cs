from model.board import Board


class Game:
    def __init__(self, player1, player2):
        self.__board = Board()
        self.player1 = player1
        self.player2 = player2

    @property
    def board(self):
        return self.__board
