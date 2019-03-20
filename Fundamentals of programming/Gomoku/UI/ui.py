from model.player import *
from controller.game import Game
import random

class UI:
    @staticmethod
    def printMenu():
        print("1. Play with computer")
        print("2. Exir")

    @staticmethod
    def start():
        while True:
            try:
                UI.printMenu()
                menu = int(input())
                if menu == 1:
                    player1 = Player(input("Introduce your name:\n"))
                    player2 = AI("Computer")
                    game = Game(player1, player2)
                    first = random.choice([1, 2])
                    current_player = first
                    print("{} starts the game".format(game.player1.name if current_player == 1 else game.player2.name))
                    while not game.board.game_won():
                        print(game.board)
                        print()
                        print()
                        if current_player == 1:
                            while True:
                                try:
                                    str = input("Introduce the coordinates for your move: ")
                                    bla = str.split(" ")
                                    x = int(bla[0])
                                    y = int(bla[1])
                                    if game.board.data[x][y] != 0:
                                        print("You can only move pieces on unoccupied cells")
                                    else:
                                        break
                                except Exception:
                                    print("Invalid move")

                        else:
                            x, y = game.player2.move(game.board)
                        game.lpo = (x, y, current_player)
                        game.board.apply_move(x, y, current_player)
                        current_player = 1 if current_player == 2 else 2
                    print("{} wins".format(game.player1.name if current_player == 2 else game.player2.name))
                elif menu == 2:
                    return
            except ValueError as e:
                print("Invalid option")

