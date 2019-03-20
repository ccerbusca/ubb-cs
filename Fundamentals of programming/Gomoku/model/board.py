from texttable import Texttable
import copy

class Point:
    """
    Represents a single cell on the board
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Board:
    """
    The game board
    """
    def __init__(self):
        self.__data = []
        for i in range(19):
            self.__data.append([0] * 19)
        self.lpo = (-1, -1, -1)

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    def copy(self):
        """
        create a copy of the board
        """
        new = Board()
        new.data = copy.deepcopy(self.__data)
        return new


    def __str__(self):
        t = Texttable()
        d = {0: " ", 1: "+", 2: "-"}
        t.header(list(range(19)))
        for i in range(19):
            lst = self.__data[i][:]
            for j in range(19):
                lst[j] = d[lst[j]] #"%d,%d" % (i, j) +
            t.add_row(lst)
        t.set_max_width(0)
        return t.draw()

    def check_vertical(self):
        """
        Verify if the last performed operation won the game in a vertical line
        :return: True if the game is over, False otehrwise
        """
        count = 0
        startx = self.lpo[0]
        starty = self.lpo[1]
        while startx >= 0 and self.__data[startx][starty] == self.lpo[2]:
            startx -= 1
        startx += 1
        while startx < 19 and self.__data[startx][starty] == self.lpo[2]:
            startx += 1
            count += 1
        return count >= 5

    def check_horizontal(self):
        """
            Verify if the last performed operation won the game in a horizontal line
            :return: True if the game is over, False otehrwise
        """
        count = 0
        startx = self.lpo[0]
        starty = self.lpo[1]
        while starty >= 0 and self.__data[startx][starty] == self.lpo[2]:
            starty -= 1
        starty += 1
        while starty < 19 and self.__data[startx][starty] == self.lpo[2]:
            starty += 1
            count += 1
        return count >= 5

    def check_diagonal_left(self):
        """
        Verify if the last performed operation won the game in a diagonal line from the left
        :return: True if the game is over, False otehrwise
        """
        count = 0
        startx = self.lpo[0]
        starty = self.lpo[1]
        while startx >= 0 and starty >= 0 and self.__data[startx][starty] == self.lpo[2]:
            startx -= 1
            starty -= 1
        startx += 1
        starty += 1
        while starty < 19 and startx < 19 and self.__data[startx][starty] == self.lpo[2]:
            startx += 1
            starty += 1
            count += 1
        return count >= 5

    def check_diagonal_right(self):
        """
        Verify if the last performed operation won the game in a diagonal line frm the right
        :return: True if the game is over, False otehrwise
        """
        count = 0
        startx = self.lpo[0]
        starty = self.lpo[1]
        while startx >= 0 and starty < 19 and self.__data[startx][starty] == self.lpo[2]:
            startx -= 1
            starty += 1
        startx += 1
        starty -= 1
        while starty >= 0 and startx < 19 and self.__data[startx][starty] == self.lpo[2]:
            startx += 1
            starty -= 1
            count += 1
        return count >= 5

    def game_won(self):
        """
        Verify if the game was won after the last performed operation
        :return: True if the game is over, False otehrwise
        """
        if self.lpo != (-1, -1, -1):
            return self.check_horizontal() or self.check_vertical() or self.check_diagonal_left() \
                    or self.check_diagonal_right()
        else:
            return False

    def apply_move(self, x, y, currentPlayer):
        """
        Apply the move on the board and save the last performed operation
        :return:
        """
        self.__data[x][y] = currentPlayer
        self.lpo = (x, y, currentPlayer)
