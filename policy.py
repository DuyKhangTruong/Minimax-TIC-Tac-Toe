from board import Board

class Policy:
    def __init__(self, shape):
        self.shape = shape

    def MakeMove(self, board, x, y):  # Make a move on board
        board.config[x][y] = self.shape

    def CheckLegal(self, board, x, y):  # Check if that move is valid
        if x > 2 or x < 0:
            return False
        if y > 2 or y < 0:
            return False

        if (board.config[x][y] != 0):
            return False

        return True

    def checkWin(self, board, x, y):
        return self.CheckVe(board, x, y) or self.CheckHoz(board, x, y) or self.CheckDiag1(board, x, y) or self.CheckDiag2(board, x, y)

    def CheckHoz(self, board, x, y):  
        count = 1
        z = y + 1
        y -= 1

        # East
        while z <= 2 and board.config[x][z] == self.shape:
            count += 1
            z += 1
            if count == 3:
                return True
        # West
        while y >= 0 and board.config[x][y] == self.shape:
            count += 1
            y -= 1
            if count == 3:
                return True

        return False

    def CheckVe(self, board, x, y):  # Check if the player has 3 in column
        count = 1
        z = x + 1
        x -= 1
        # South
        while z <= 2 and board.config[z][y] == self.shape:
            count += 1
            z += 1
            if count == 3:
                return True

        # North
        while x >= 0 and board.config[x][y] == self.shape:
            count += 1
            x -= 1
            if count == 3:
                return True
        return False

    def CheckDiag1(self, board, x, y):
        count = 1
        i, j = x, y
        i += 1
        j -= 1
        x -= 1
        y += 1

        while (i <= 2 and j >= 0) and board.config[i][j] == self.shape:
            count += 1
            i += 1
            j -= 1
            if count == 3:
                return True

        while (x >= 0 and y <= 2) and board.config[x][y] == self.shape:
            count += 1
            x -= 1
            y += 1
            if count == 3:
                return True
        return False

    def CheckDiag2(self, board, x, y):
        count = 1
        i, j = x, y
        i -= 1
        j -= 1
        x += 1
        y += 1

        while (i >= 0 and j >= 0) and board.config[i][j] == self.shape:
            count += 1
            i -= 1
            j -= 1
            if count == 3:
                return True
        while (x <= 2 and y <= 2) and board.config[x][y] == self.shape:
            count += 1
            x -= 1
            y += 1
            if count == 3:
                return True
        return False
