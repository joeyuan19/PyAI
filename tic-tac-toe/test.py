import matplotlib.pyplot as plt
from game import TicTacToe
from players import * 

player = RealPlayer('Joe')
player1 = TicTacToePlayer('Mem Bot')
player2 = RandomBot('Rando Bot')

wins1,ties1,losses1 = [],[],[]
wins2,ties2,losses2 = [],[],[]

player1.set_weights(25,-50,-75)

N = 10000
for n in range(N):
    TicTacToe(player1,player2).play()
    w,t,l = player1.get_stats()
    wins1.append(w)
    ties1.append(t)
    losses1.append(l)
    w,t,l = player2.get_stats()
    wins2.append(w)
    ties2.append(t)
    losses2.append(l)

N = list(range(1,N+1))
f1 = plt.figure(1)
ax = f1.add_subplot(111)
ax.set_title(player1.name)
ax.plot(N,wins1,'r',label='wins')
ax.plot(N,ties1,'g',label='ties')
ax.plot(N,losses1,'b',label='losses')
ax.legend()

f2 = plt.figure(2)
ax = f2.add_subplot(111)
ax.set_title(player2.name)
ax.plot(N,wins2,'r',label='wins')
ax.plot(N,ties2,'g',label='ties')
ax.plot(N,losses2,'b',label='losses')
ax.legend()
plt.show()

player1.print_status()
player2.print_status()

while True:
    try:
        TicTacToe(player,player1).play(no_print=False)
    except KeyboardInterrupt:
        break
