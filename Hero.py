import WConio2
from Character import Character
#teste
class Hero(Character):
    #método construtor
    def __init__(self):
        self.icon = ['██'] #2 caracteres █ que é 0 219 na ascii
        self.position = [1,15] #lista[x,y]
        self.speed = 3
        self.last_move = ''

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

    def _moveLeft(self,frame_width, frame_height):
        if self.position[0] != 1:
            self.position[0] = self.position[0] - 1

    def _moveRight(self,frame_width, frame_height):
        if self.position[0] != frame_width - 3:
            self.position[0] = self.position[0] + 1

    def _moveUp(self,frame_width, frame_height):
        if self.position[1] != 1:
            self.position[1] = self.position[1] - 1

    def _moveDown(self,frame_width, frame_height):
        if self.position[1] != frame_height - 1:
            self.position[1] = self.position[1] + 1

    def _attHitbox(self):
        self.hitbox["a"] = self.position
        self.hitbox["b"] = [self.position[0]+1, self.position[1]]
            
    #TODO metodos teleporteUp, Down, etc 
    def _teleport(self, frame_width, frame_height):
        #TODO trocar o match case pelo dicionario de funcoes de telporte quando o mesmo estiver pronto
        
        match self.last_move:
            case 'a':
                if self.position[0] - 8 >= 1:
                    self.position[0] = self.position[0] - 8
            case 'd':
                if self.position[0] + 8 <= frame_width - 2:
                    self.position[0] = self.position[0] + 8
            case 'w':
                if self.position[1] - 4 >= 1:
                    self.position[1] = self.position[1] - 4
            case 's':
                if self.position[1] + 4 <= frame_height - 2:
                    self.position[1] = self.position[1] + 4

    def move(self,key,frame_width, frame_height):
        movement = self.acceptedMoves[key]
        movement(frame_width, frame_height)
        self._attHitbox()

    #TODO def getHitbox():

    #TODO def getPosition():