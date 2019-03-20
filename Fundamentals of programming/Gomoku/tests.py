import unittest
import os
from datetime import datetime
from controller.game import Game
from model.player import AI, Player


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game(Player("Player"), AI("Computer"))


    def tearDown(self):
        del self.game

    def testApplyMove(self):
        self.game.board.apply_move(10, 10, 1)
        self.assertEqual(self.game.board.data[10][10], 1, "The move wasn't applied on the board")

    def testGameWon(self):
        self.game.board.apply_move(10, 10, 1)
        self.game.board.apply_move(10, 11, 1)
        self.game.board.apply_move(10, 12, 1)
        self.game.board.apply_move(10, 13, 1)
        self.game.board.apply_move(10, 14, 1)
        self.assertEqual(self.game.board.game_won(), True, "The game is not considered over")





if __name__ == "__main__":
    unittest.main()