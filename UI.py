#UI.py
class UI:
    def __init__(self):
        self.board = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}

    def displayBoard(self):
    
            
        str_1 = self.board[1]+' | ' + self.board[2]+' | ' +self.board[3]
        str_2 = self.board[4]+' | ' + self.board[5]+' | ' +self.board[6]
        str_3 = self.board[7]+' | ' + self.board[8]+' | ' +self.board[9]

        print('\n{: >15}'.format(str_1))
        print('{: >15}'.format('-'*9))
        print('{: >15}'.format(str_2))
        print('{: >15}'.format('-'*9))
        print('{: >15}\n'.format(str_3))
