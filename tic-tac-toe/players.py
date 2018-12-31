from pyAI import *
import random

def TTTRealPlayer(RealPlayer):
    def parse_move(self,user_input):
        n,m = map(int,input(user_input).split())
        while board[n*3 + m] != 0:
            print('Spot taken, choose again')
            n,m = map(int,input('Input move: (e.g 0 0)\n').split())
        return n*3 + m

def TTTMemoryBot(
    moves = [i for i,j in enumerate(board) if j == 0]
