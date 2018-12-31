import random

class Board(object):
    def __init__(self):
        pass
    
    def copy(self):
        raise NotImplementedError("Method <copy> is not implemented for "+str(self.__class__))

class Player(object):
    def __init__(self,name):
        self.name = name
        self.wins   = 0
        self.ties   = 0
        self.losses = 0

    def set_player(self,player):
        self.player = player
    
    def report_winner(self,winner,board):
        self.winner = winner
        if self.player == winner:
            self.wins   += 1
        elif winner == 0:
            self.ties   += 1
        else:
            self.losses += 1
    
    def print_status(self):
        print(self.name,'wins='+str(self.wins),'ties='+str(self.ties),'losses='+str(self.losses))

    def get_stats(self):
        """Returns the stored number of wins, ties, and losses"""
        return self.wins,self.ties,self.losses

    def get_moves(self,board):
        """Returns a list of valid moves allowed given the current state of the board
        Method is game specific
        """
        raise NotImplementedError("Method <get_moves> is not implemented for "+str(self.__class__))
    
    def get_move(self,board):
        """Returns the next move a player makes"""
        moves = self.get_moves(board)
        return self.pick_move(moves,board)

    def pick_move(self,moves,board):
        """Chooses next move from available moves
        Method is game specific
        """
        raise NotImplementedError("Method <pick_move> is not implemented for "+str(self.__class__))
        
    def save_state(self):
        """Saves the state of the player"""
        raise NotImplementedError("Method <save_state> is not implemented for "+str(self.__class__))

class RealPlayer(Player):
    def parse_move(self,user_input):
        """Returns the parsed user input for a real player as a usable move
        Method is game specific
        """
        raise NotImplementedError("Method <parse_move> is not implemented for "+str(self.__class__))
    
    def get_move(self,board,show_board=True):
        """Returns the move a real player chooses in a usable form
        Method is game specific
        """
        if show_board:
            print(board)
        return self.parse_move(raw_input('Please Input Move:'+self.move_example))

class RandomBot(Player):
    def pick_move(self,moves):
        """Returns the randomly selected move"""
        return random.choice(moves)

class RandomMemoryBot(Player):
    def __init__(self,*args,**kwargs):
        self.states       = {}
        self.current_game = []
        self.weight_win   = 1
        self.weight_tie   = 1
        self.weight_loss  = -1
        super().__init__(*args,**kwargs)
    
    def set_weights(self,w,t,l):
        self.weight_win   = w
        self.weight_tie   = t
        self.weight_loss  = l
    
    def pick_move(self,moves,board):
        odds  = []
        for move in moves:
            _board= board.copy()
            _board[move] = self.player
            state = ''.join(str(i) for i in _board)
            if state in self.states:
                r = self.get_rating(state)
                odds.append((r,move))
            else:
                odds.append((0,move))
        odds = sorted(odds)
        moves = [move[1] for move in odds if odds[-1][0] == move[0]]
        move = random.choice(moves)
        _board = board.copy()
        _board[move] = self.player
        state = ''.join(str(i) for i in _board)
        self.current_game.append(state)
        return move
    
    def report_winner(self,winner,board):
        super().report_winner(winner,board)
        win  = winner == self.player
        tie  = winner == 0
        loss = not (win or tie)
        for state in self.current_game:
            if state in self.states:
                self.states[state]['win']   += win
                self.states[state]['tie']   += tie
                self.states[state]['loss']  += loss
                self.states[state]['total'] += 1
            else:
                self.states[state] = {
                    'win'   : win,
                    'tie'   : tie,
                    'loss'  : loss,
                    'total' : 1
                }
        self.current_game = []
    
    def get_rating(self,state):
        r  = self.weight_win  * self.states[state]['win']
        r += self.weight_tie  * self.states[state]['tie']
        r += self.weight_lose * self.states[state]['lose']
        return r
