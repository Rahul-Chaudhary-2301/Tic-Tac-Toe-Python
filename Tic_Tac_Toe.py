#Tic Tac Toe
from Player import Player
from UI import UI
from Game import Game

if __name__ == '__main__':
    print('Wellcome to X O')
    print(' 1] Play with CPU\n 2] Play with Human \n 3]Exit')
    opt = int(input('>'))
    if opt == 1:
        pass
        sel = input('Select X / O : ')
        if sel == 'X':
            Player1 = Player('X')
            Computer = Player('O','COMPUTER')
            Board = UI()
            G = Game(Player1,Computer,Board,mode='C')
            G.play()
        else:
            Player2 = Player('O')
            Computer = Player('X','COMPUTER')
            Board = UI()
            G = Game(Computer,Player2,Board,mode='C')
            G.play()
    elif opt == 2:
        Player1 = Player('X')
        Player2 = Player('O')
        Board = UI()
        G = Game(Player1,Player2,Board,mode='H')
        G.play()
    elif opt == 3:
        exit()
        
        
        
        
        
        
