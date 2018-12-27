import random

class IllegalMoveError(Exception):
    pass

class TicTacToe(object):
    def __init__(self,player_1,player_2):
        self.board     = [0]*9
        self.p1        = player_1
        self.p1.set_player(1)
        self.p2        = player_2
        self.p2.set_player(2)
        self.winner    = -1
        self.no_winner = True

    def play(self,no_print=True):
        turn = True
        while self.no_winner:
            if turn:
                m = self.p1.get_move(self.board)
            else:
                m = self.p2.get_move(self.board)
            if self.board[m] != 0:
                raise IllegalMoveError('Illegal move by player '+str(1+(not turn))+' <'+str(m//3)+','+str(m%3)+'>')
            self.board[m] = 1+(not turn) 
            turn = not turn
            self.check_winner()
        self.p1.report_winner(self.winner,self.board)
        self.p2.report_winner(self.winner,self.board)
        if not no_print:
            print({0:'Tie',1:'Winner '+self.p1.name,2:'Winner '+self.p2.name}[self.winner])
            for n in range(3):
                print(' '.join(str(self.board[n*3+i]) for i in range(3)))
        return self.winner
    
    def check_winner(self):
        if 0 != self.board[0] == self.board[1] == self.board[2]:
            self.winner    = self.board[0]
            self.no_winner = False
        elif 0 != self.board[3] == self.board[4] == self.board[5]:
            self.winner    = self.board[3]
            self.no_winner = False
        elif 0 != self.board[6] == self.board[7] == self.board[8]:
            self.winner    = self.board[6]
            self.no_winner = False
        elif 0 != self.board[0] == self.board[3] == self.board[6]:
            self.winner    = self.board[0]
            self.no_winner = False
        elif 0 != self.board[1] == self.board[4] == self.board[7]:
            self.winner    = self.board[1]
            self.no_winner = False
        elif 0 != self.board[2] == self.board[5] == self.board[8]:
            self.winner    = self.board[2]
            self.no_winner = False
        elif 0 != self.board[0] == self.board[4] == self.board[8]:
            self.winner    = self.board[0]
            self.no_winner = False
        elif 0 != self.board[2] == self.board[4] == self.board[6]:
            self.winner    = self.board[2]
            self.no_winner = False
        elif self.board.count(0) == 0:
            self.winner    = 0
            self.no_winner = False


