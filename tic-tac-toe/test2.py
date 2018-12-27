import matplotlib.pyplot as plt
import numpy as np
from game import TicTacToe
from players import * 

wins,ties,losses = [],[],[]

win_weight = []

N = 1000

for w in np.linspace(-100,100,100):
    player1 = RandomMemoryBot('Mem Bot')
    player1.set_weights(25,-50,-75)
    player2 = RandomMemoryBot('Rando Bot')
    player2.set_weights(25,-50,-75)
    win_weight.append(w)
    for n in range(N):
        TicTacToe(player1,player2).play()
        w,t,l = player2.get_stats()
    w,t,l = player1.get_stats()
    wins.append(w)
    ties.append(t)
    losses.append(l)
plt.plot(win_weight,wins,'r',label='wins')
plt.plot(win_weight,ties,'b',label='ties')
plt.plot(win_weight,losses,'g',label='losses')
plt.legend()
plt.show()
