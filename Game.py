#GAME.PY
from CPU import CPU_play
class Game:
    def __init__(self,Player1,Player2,Board,mode):
        self.player1 = Player1
        self.player2 = Player2
        self.board = Board
        self.mode = mode
        self.covered_tile = []
        self.curr_player = None


    ##    It return the number of total element in the board
    ##    For example:
    ##    Board --> {['X',2,3]
    ##               [4,5,'O']
    ##               ['X','O',9]
    ##               }
    ##    Then checkBoard will return 7
    ##    as checkBoard only consider the elements only once.
    def checkBoard(self):
        boardItem = self.board.board.values()
        return len(set(boardItem))


    ##    It is a method used to check is the tile is valid for placing an element or not
    ##    It return the a message if X or O is already present on the tile
    ##    If the tile is valid then it will replace the element on the tile to [X or O]
    def checkValidTile(self,data,player):
        if data not in self.covered_tile:
            self.covered_tile.append(data)
            self.board.board[data] = player.value
        else:
            print('Invalid section of tile')
            print('Element Present')
            return self.get(self.curr_player)
        
    ##    This function is used for taking the the input from the user and validating it
    def get(self,player,player_type = None):
        print("+{:-^35}+".format('-'))
        if player_type != None:
            inp = player_type.play(player,self.board)
            print('|  '+player.name," [tile no] -> ",inp)
        else:
            print('|  '+player.name + ' [tile no] -> ',end='')
            inp = int(input())
        print("+{:-^35}+".format('-'))
        self.checkValidTile(inp,player)


    ##    This function is used for changing the player after a player enter it data
    def checkPlayer(self):
        if self.curr_player == None:
            self.curr_player = self.player1
        elif self.curr_player == self.player1:
            self.curr_player = self.player2
        else:
            self.curr_player = self.player1

            
    ##    This function check the winner of the game 
    def checkWinner(self):
        boardItem = list(self.board.board.values())
        win_comb = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        for i in win_comb:
            s = [boardItem[j-1] for j in i]
            if s == ['X','X','X'] or s == ['O','O','O']:
                self.board.displayBoard()
                print("------ Winner = "+self.curr_player.name)
                return 2
        return self.checkBoard()
                            
    def play(self):
        check = self.checkBoard()
        if self.mode == 'C':
            computer = CPU_play()
        while check != 2:
            self.board.displayBoard()
            self.checkPlayer()
            if self.curr_player.name == 'COMPUTER':
                self.get(self.curr_player,computer)
            else:
                self.get(self.curr_player)
            check = self.checkWinner()
        if  self.checkBoard() == 2:
                self.board.displayBoard()
                print("Match Draw") 
