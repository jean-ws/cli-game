import WConio2
from Character import Character
#teste
class Hero(Character):
    #método construtor
    def __init__(self):
        self.icon = ['██'] #2 caracteres █ que é 0 219 na ascii
        self.position = [9,15] #lista[x,y]

        #hitbox[char] == [x,y]
        self.hitbox = {
            'a' : self.position,
            'b' : [self.position[0] + 1, self.position[1]]
        }

        self.acceptedMoves = {
            'a': self._moveLeft,
            'd': self._moveRight,
            'w': self._moveUp,
            's': self._moveDown,
            ' ': self._teleport
        }

        self.teleport = {
            'a': self._teleportLeft,
            'd': self._teleportRight,
            'w': self._teleportUp,
            's': self._teleportDown
        }

