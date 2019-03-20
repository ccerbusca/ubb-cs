from model.board import Point

class Player:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

class AI(Player):
    @staticmethod
    def calculate_score(consecutive, open_ends):
        """
        Calculate the score of a set of pieces
        :param consecutive: number of consecutive pieces
        :param open_ends: number of open ends
        :return: the score of the state
        """
        if open_ends == 0 and consecutive < 5:
            return 0
        if consecutive == 4:
            if open_ends == 1:
                return 500000
            elif open_ends == 2:
                return 1000000
        elif consecutive == 3:
            if open_ends == 1:
                return 7
            elif open_ends == 2:
                return 10000
        elif consecutive == 2:
            if open_ends == 1:
                return 2
            elif open_ends == 2:
                return 5
        elif consecutive == 1:
            if open_ends == 1:
                return 0.5
            elif open_ends == 2:
                return 1
        else:
            return 2000000000

    @staticmethod
    def calculate_overall_score(board, player):
        """
        Calculate the overall score for the whole table of the specified player
        :param board: the board
        :param player: player id
        :return: overall score
        """
        def calculate_score_horizontal():
            score = 0
            countConsecutive = 0
            openEnds = 0
            i = 0
            while i < 19:
                j = 0
                while j < 19:
                    if board.data[i][j] == player:
                        countConsecutive += 1
                    elif board.data[i][j] == 0 and countConsecutive > 0:
                        openEnds += 1
                        score += AI.calculate_score(countConsecutive, openEnds)
                        countConsecutive = 0
                        openEnds = 1
                    elif board.data[i][j] == 0:
                        openEnds = 1
                    elif countConsecutive > 0:
                        score += AI.calculate_score(countConsecutive, openEnds)
                        countConsecutive = 0
                        openEnds = 0
                    j += 1
                if countConsecutive > 0:
                    score += AI.calculate_score(countConsecutive, openEnds)
                countConsecutive = 0
                openEnds = 0
                i += 1
            return score
        def calculate_score_vertical():
            score = 0
            countConsecutive = 0
            openEnds = 0
            j = 0
            while j < 19:
                i = 0
                while i < 19:
                    if board.data[i][j] == player:
                        countConsecutive += 1
                    elif board.data[i][j] == 0 and countConsecutive > 0:
                        openEnds += 1
                        score += AI.calculate_score(countConsecutive, openEnds)
                        countConsecutive = 0
                        openEnds = 1
                    elif board.data[i][j] == 0:
                        openEnds = 1
                    elif countConsecutive > 0:
                        score += AI.calculate_score(countConsecutive, openEnds)
                        countConsecutive = 0
                        openEnds = 0
                    i += 1
                if countConsecutive > 0:
                    score += AI.calculate_score(countConsecutive, openEnds)
                countConsecutive = 0
                openEnds = 0
                j += 1
            return score
        def calculate_score_diagonal_left():
            score = 0
            countConsecutive = 0
            openEnds = 0
            for i in range(16):
                j = 0
                while j < 19 and i < 19:
                    if board.data[i][j] == player:
                        countConsecutive += 1
                    elif board.data[i][j] == 0 and countConsecutive > 0:
                        openEnds += 1
                        score += AI.calculate_score(countConsecutive, openEnds)
                        countConsecutive = 0
                        openEnds = 1
                    elif board.data[i][j] == 0:
                        openEnds = 1
                    elif countConsecutive > 0:
                        score += AI.calculate_score(countConsecutive, openEnds)
                        countConsecutive = 0
                        openEnds = 0
                    j += 1
                    i += 1
                if countConsecutive > 0:
                    score += AI.calculate_score(countConsecutive, openEnds)
                countConsecutive = 0
                openEnds = 0
            countConsecutive = 0
            openEnds = 0
            for j in range(1, 16):
                i = 0
                while i < 19 and j < 19:
                    if board.data[i][j] == player:
                        countConsecutive += 1
                    elif board.data[i][j] == 0 and countConsecutive > 0:
                        openEnds += 1
                        score += AI.calculate_score(countConsecutive, openEnds)
                        countConsecutive = 0
                        openEnds = 1
                    elif board.data[i][j] == 0:
                        openEnds = 1
                    elif countConsecutive > 0:
                        score += AI.calculate_score(countConsecutive, openEnds)
                        countConsecutive = 0
                        openEnds = 0
                    i += 1
                    j += 1
                if countConsecutive > 0:
                    score += AI.calculate_score(countConsecutive, openEnds)
                countConsecutive = 0
                openEnds = 0
            return score
        def calculate_score_diagonal_right():
            score = 0
            countConsecutive = 0
            openEnds = 0
            for i in range(15, -1, -1):
                j = 18
                while j >= 0 and i < 19:
                    if board.data[i][j] == player:
                        countConsecutive += 1
                    elif board.data[i][j] == 0 and countConsecutive > 0:
                        openEnds += 1
                        score += AI.calculate_score(countConsecutive, openEnds)
                        countConsecutive = 0
                        openEnds = 1
                    elif board.data[i][j] == 0:
                        openEnds = 1
                    elif countConsecutive > 0:
                        score += AI.calculate_score(countConsecutive, openEnds)
                        countConsecutive = 0
                        openEnds = 0
                    j -= 1
                    i += 1
                if countConsecutive > 0:
                    score += AI.calculate_score(countConsecutive, openEnds)
                countConsecutive = 0
                openEnds = 0
            countConsecutive = 0
            openEnds = 0
            for j in range(14, -1, -1):
                i = 0
                while i < 19 and j >= 0:
                    if board.data[i][j] == player:
                        countConsecutive += 1
                    elif board.data[i][j] == 0 and countConsecutive > 0:
                        openEnds += 1
                        score += AI.calculate_score(countConsecutive, openEnds)
                        countConsecutive = 0
                        openEnds = 1
                    elif board.data[i][j] == 0:
                        openEnds = 1
                    elif countConsecutive > 0:
                        score += AI.calculate_score(countConsecutive, openEnds)
                        countConsecutive = 0
                        openEnds = 0
                    i += 1
                    j -= 1
                if countConsecutive > 0:
                    score += AI.calculate_score(countConsecutive, openEnds)
                countConsecutive = 0
                openEnds = 0
            return score
        return calculate_score_horizontal() + calculate_score_vertical() + calculate_score_diagonal_left() + \
               calculate_score_diagonal_right()

    def move(self, board):
        """
        Calculate the computer's next move
        :param board: board
        :return: pair of coordinates for the next move
        """
        max_point = Point(-1, -1)
        max_score = -100
        i = 0
        while i < 19:
            j = 0
            while j < 19:
                if board.data[i][j] == 0:
                    new_board = board.copy()
                    new_board.apply_move(i, j, 2)
                    AIScore = AI.calculate_overall_score(new_board, 2)
                    UserScore = AI.calculate_overall_score(new_board, 1)
                    if AIScore > UserScore and AIScore - UserScore > max_score:
                        max_score = AIScore - UserScore
                        max_point = Point(i, j)
                j += 1
            i += 1
        return max_point.x, max_point.y
