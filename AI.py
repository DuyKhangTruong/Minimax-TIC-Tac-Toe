import math

from policy import Policy
from board import Board


class AI:
    def __init__(self, computerShape):
       self.computerShape = computerShape
       self.computer = Policy(self.computerShape)
       self.humanShape = "X"
       self.human = Policy(self.humanShape)
       self.point = {"Computer": 10, "Human": -10, "Tie":0}


    def moveLeft(self, board):
        return not(board.isFull())
    
    def validMoves(self,board):
        moves = []
        for i in range(board.row):
            for j in range(board.column):
                if board.config[i][j] == 0:
                    pass
        pass
    
    def Win(self, shape):
        winner = Policy(shape)
        return winner.checkWin(board,x,y)

    def Evaluate(self, board, isMaximizing, x, y):
        if isMaximizing:
            if self.computer.checkWin(board,x,y):
                return "Computer"
        else:
            if self.human.checkWin(board,x,y):
                return "Human"
        return "Tie"
        
    
    def miniMax(self,board,depth,isMaximizing,x,y):
        score = self.point[self.Evaluate(board,not(isMaximizing),x,y)]

        if score == 10:
            return score - depth

        elif score == -10:
            return score + depth

        if self.moveLeft(board) == False:
            return 0
        
        if isMaximizing:
            bestScore = -math.inf 
            for x in range(board.row):
                for y in range(board.column):
                    if board.config[x][y] == 0:
                        board.config[x][y] = self.computerShape
                        score = self.miniMax(board,depth +1, not(isMaximizing),x,y)
                        bestScore = max(score,bestScore)
                        board.config[x][y] = 0
            
            return bestScore
        else:
            bestScore = math.inf 
            for i in range(board.row):
                for j in range(board.column):
                    if board.config[i][j] == 0:
                        board.config[i][j] = self.humanShape
                        score = self.miniMax(board,depth +1, not(isMaximizing),i,j)
                        bestScore = min(score,bestScore)
                        board.config[i][j] = 0
            
            return bestScore

    
    def findBestMove(self, board):
        bestScore = -math.inf
        row = int()
        column =  int()

        for i in range(board.row):
            for j in range(board.column):
                pos = board.config[i][j]
                if pos == 0:
                    board.config[i][j] = self.computerShape
                    currentScore = self.miniMax(board,0,False,i,j)
                    #print("Computer evals this move: " + str(currentScore))
                    board.config[i][j] = 0
                    if currentScore > bestScore:
                        row = i
                        column = j
                        bestScore = currentScore

        return [row, column]
    
    


                    



