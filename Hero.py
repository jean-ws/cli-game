import WConio2
from Character import Character
#teste
class Hero(Character):
    #método construtor
    def __init__(self):
        self.icon = ['██'] #2 caracteres █ que é 0 219 na ascii
        self.position = [9,15] #lista[x,y]
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

        self.teleport = {
            'a': self._teleportLeft,
            'd': self._teleportRight,
            'w': self._teleportUp,
            's': self._teleportDown
        }

        #TODO dicionario com as funcoes teleporteUp, Down, etc (valores) de acordo com a ultima tecla pressionada (chaves) para nao precisar usar condicional no _teleporte()

    def _attHitbox(self):
        self.hitbox["a"] = self.position
        self.hitbox["b"] = [self.position[0]+1, self.position[1]]
    
    def _teleportLeft(self,frame_width,frame_height):
        if self.position[0] - 8 >= 1:
            self.position[0] = self.position[0] - 8
    
    def _teleportRight(self,frame_width,frame_height):
        if self.position[0] + 8 <= frame_width - 2:
            self.position[0] = self.position[0] + 8
    
    def _teleportUp(self,frame_width,frame_height):
        if self.position[1] - 4 >= 1:
            self.position[1] = self.position[1] - 4
    
    def _teleportDown(self,frame_width,frame_height):
        if self.position[1] + 4 <= frame_height - 2:
            self.position[1] = self.position[1] + 4
            
    def _teleport(self, frame_width, frame_height):
        teleport = self.teleport[self.last_move]
        teleport(frame_width,frame_height)
    

    def move(self,key,frame_width, frame_height):
        if key in self.acceptedMoves:
            movement = self.acceptedMoves[key]
            movement(frame_width, frame_height)
            self._attHitbox()

    #TODO def getHitbox():

    #TODO def getPosition():