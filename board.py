class Board:
    def __init__(self):  # 15x15 board
        self.row = 3
        self.column = 3
        # create board
        self.config = [[0 * y for y in range(self.column)]
                       for x in range(self.row)]

    def DrawBoard(self):
        horizontal_sym = '-------'
        for i in range(self.column):
            horizontal_sym += '\n' + '|'
            for j in range(self.row):
                pos = self.config[i][j]
                if pos == 0:
                    pos = ' '
                horizontal_sym += str(pos) + '|'
        horizontal_sym += '\n-------'
        return horizontal_sym

    def isFull(self):
        for i in range(self.row):
            for j in range(self.column):
                if self.config[i][j] == 0:
                    return False
        return True

