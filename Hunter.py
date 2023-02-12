from Character import Character

from Character import Character
#teste
class Hunter(Character):
    #método construtor
    def __init__(self):
        self.icon = ['██'] #2 caracteres █ que é 0 219 na ascii
        self.position = [12,15] #lista[x,y]

        #hitbox[char] == [x,y]
        self.hitbox = {
            'a' : self.position,
            'b' : [self.position[0] + 1, self.position[1]]
        }

        self.acceptedMoves = {
            'j': self._moveLeft,
            'l': self._moveRight,
            'i': self._moveUp,
            'k': self._moveDown,
            ';': self._teleport
        }

        self.teleport = {
            'j': self._teleportLeft,
            'l': self._teleportRight,
            'i': self._teleportUp,
            'k': self._teleportDown
        }
