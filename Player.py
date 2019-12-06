#Player.py
class Player:
    def __init__(self,value,name=None):
        if name == None:
            print("Player name : ")
            name = input()
        self.name = name
        self.value = value
