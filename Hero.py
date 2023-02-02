import WConio2
from Character import Character
#teste
class Hero(Character):
    #método construtor
    def __init__(self):
        self.icon = ['██'] #2 caracteres █ que é 0 219 na ascii
        self.position = [1,15] #lista[x,y]
        self.speed = 3
        self.ultimo_movimento = ''

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

        #TODO dicionario com as funcoes teleporteUp, Down, etc (valores) de acordo com a ultima tecla pressionada (chaves) para nao precisar usar condicional no _teleporte()

    def _attHitbox(self):
        self.hitbox["a"] = self.position
        self.hitbox["b"] = [self.position[0]+1, self.position[1]]
            
    #TODO metodos teleporteUp, Down, etc 
    def _teleport(self):
        #TODO trocar o match case pelo dicionario de funcoes de telporte quando o mesmo estiver pronto
        match self.last_move:
            case 'a':
                self.position[0] = self.position[0] - 9
            case 'd':
                self.position[0] = self.position[0] + 9
            case 'w':
                self.position[1] = self.position[1] - 4
            case 's':
                self.position[1] = self.position[1] + 4

    def move(self,key):
        movement = self.acceptedMoves[key]
        movement()
        self._attHitbox()

    #TODO def getHitbox():

    #TODO def getposition():