from shutil import move
from Character import Character

#TODO classe de todos inimigos
class Enemy(Character):
    #atributos que TODOS inimigos terão
    pass

class NormalEnemy(Enemy):
    #atributos que somente o inimigo normal terá

    def __init__(self):
        self.icon = ["##","##"] #lista[linha de cima, linha de baixo]
        self.position = [2,5] #lista[x,y]
        self.speed = 14
        self.acceptedMoves = {
            'x-': self._moveLeft,
            'x+': self._moveRight,
            'y-': self._moveUp,
            'y+': self._moveDown,
            }

        self.hitbox = {
            'a' : self.position,
            'b' : [self.position[0] + 1, self.position[1]],
            'c' : [self.position[0], self.position[1] + 1],
            'd' : [self.position[0] + 1,self.position[1] + 1]
        }
    
    def _attHitbox(self):
        self.hitbox = {
            'a' : self.position,
            'b' : [self.position[0] + 1, self.position[1]],
            'c' : [self.position[0], self.position[1] + 1],
            'd' : [self.position[0] + 1,self.position[1] + 1]
        }

    def trackHero(self,hero):
        
        if hero.position[0] > self.position[0]:
            movement = 'x+'
        elif hero.position[0] < self.position[0]:
            movement = 'x-'
        elif hero.position[1] > self.position[1]:
            movement = 'y+'
        elif hero.position[1] < self.position[1]:
            movement = 'y-'
        
        return movement

    def move(self,hero,frame_width, frame_height):
        movement = self.trackHero(hero)
        action = self.acceptedMoves[movement]
        action(frame_width, frame_height)
        self._attHitbox()
        
    #TODO metodo que segue o heroi (usar velocidade)