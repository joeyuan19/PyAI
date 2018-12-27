from game import 
import random

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
        return self.wins,self.ties,self.losses

    def new_game(self):
        pass
    
    def get_moves(self):

class RealPlayer(Player):
    def get_move(self,board):
        for n in range(3):
            print(' '.join(str(board[n*3+i]) for i in range(3)))
        n,m = map(int,input('Input move: (form "row col": e.g 0 0)\n').split())
        while board[n*3 + m] != 0:
            print('Spot taken, choose again')
            n,m = map(int,input('Input move: (e.g 0 0)\n').split())
        return n*3 + m

class RandomBot(Player):
    def get_move(self,board):
        return random.choice([i for i,j in enumerate(board) if j == 0])

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
    
    def get_move(self,board):
    
    def get_move(self,moves,board):
        odds  = []
        for move in moves:
            _board = [i for i in board]
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
        _board = [i for i in board]
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
        r = self.weight_win*self.states[state]['win']
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
        return self.wins,self.ties,self.losses

    def new_game(self):
        pass

class RealPlayer(Player):
    def get_move(self,board):
        for n in range(3):
            print(' '.join(str(board[n*3+i]) for i in range(3)))
        n,m = map(int,input('Input move: (form "row col": e.g 0 0)\n').split())
        while board[n*3 + m] != 0:
            print('Spot taken, choose again')
            n,m = map(int,input('Input move: (e.g 0 0)\n').split())
        return n*3 + m

class RandomBot(Player):
    def get_move(self,board):
        return random.choice([i for i,j in enumerate(board) if j == 0])

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
    
    def get_move(self,board):
        moves = [i for i,j in enumerate(board) if j == 0]
        odds  = []
        for move in moves:
            _board = [i for i in board]
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
        _board = [i for i in board]
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
        r = self.weight_win*self.states[state]['win']
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
        return self.wins,self.ties,self.losses

    def new_game(self):
        pass

class RealPlayer(Player):
    def get_move(self,board):
        for n in range(3):
            print(' '.join(str(board[n*3+i]) for i in range(3)))
        n,m = map(int,input('Input move: (form "row col": e.g 0 0)\n').split())
        while board[n*3 + m] != 0:
            print('Spot taken, choose again')
            n,m = map(int,input('Input move: (e.g 0 0)\n').split())
        return n*3 + m

class RandomBot(Player):
    def get_move(self,board):
        return random.choice([i for i,j in enumerate(board) if j == 0])

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
    
    def get_move(self,board):
        moves = [i for i,j in enumerate(board) if j == 0]
        odds  = []
        for move in moves:
            _board = [i for i in board]
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
        _board = [i for i in board]
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
        r = self.weight_win*self.states[state]['win']
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
        return self.wins,self.ties,self.losses

    def new_game(self):
        pass

class RealPlayer(Player):
    def get_move(self,board):
        for n in range(3):
            print(' '.join(str(board[n*3+i]) for i in range(3)))
        n,m = map(int,input('Input move: (form "row col": e.g 0 0)\n').split())
        while board[n*3 + m] != 0:
            print('Spot taken, choose again')
            n,m = map(int,input('Input move: (e.g 0 0)\n').split())
        return n*3 + m

class RandomBot(Player):
    def get_move(self,board):
        return random.choice([i for i,j in enumerate(board) if j == 0])

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
    
    def get_move(self,board):
        moves = [i for i,j in enumerate(board) if j == 0]
        odds  = []
        for move in moves:
            _board = [i for i in board]
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
        _board = [i for i in board]
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
        r = self.weight_win*self.states[state]['win']
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
        return self.wins,self.ties,self.losses

    def new_game(self):
        pass

class RealPlayer(Player):
    def get_move(self,board):
        for n in range(3):
            print(' '.join(str(board[n*3+i]) for i in range(3)))
        n,m = map(int,input('Input move: (form "row col": e.g 0 0)\n').split())
        while board[n*3 + m] != 0:
            print('Spot taken, choose again')
            n,m = map(int,input('Input move: (e.g 0 0)\n').split())
        return n*3 + m

class RandomBot(Player):
    def get_move(self,board):
        return random.choice([i for i,j in enumerate(board) if j == 0])

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
    
    def get_move(self,board):
        moves = [i for i,j in enumerate(board) if j == 0]
        odds  = []
        for move in moves:
            _board = [i for i in board]
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
        _board = [i for i in board]
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
        r = self.weight_win*self.states[state]['win']
        r += self.weight_tie*self.states[state]['tie']
        r += self.weight_loss*self.states[state]['loss']
        return r

    def train(self,N,other_player):
        pass
        
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
    
    def get_move(self,moves,board):
        moves = self.get_moves(board)
        odds  = []
        for move in moves:
            _board = [i for i in board]
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
        _board = [i for i in board]
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
        r = self.weight_win*self.states[state]['win']
        r += self.weight_tie*self.states[state]['tie']
        r += self.weight_loss*self.states[state]['loss']
        return r

    def train(self,N,other_player):
        pass
        
    def save_history(self):
        pass

